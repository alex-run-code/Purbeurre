import mysql.connector
import config

# Initializing database
mydb = mysql.connector.connect(
  host=config.DB_HOST,
  user=config.DB_USER,
  passwd=config.DB_PASSWD
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("USE PurBeurredb")


# This function display the initial terminal
def display_terminal():
    loop = True
    while loop is True:
        choice = input ("\nSelectionnez un menu \n"
        "1- Voir la liste des catégories \n"
        "2- Voir mes aliments substitués \n"
        "3- Fermer le programme \n"
        "\nVotre choix: ")
        if choice == "1":
            display_categories()
        elif choice =="2":
            display_saved_food()
        elif choice =='3':
            loop = False
        else: 
            print("Veuillez selectionner un menu en entrant un chiffre")
        
# This function display the categories
def display_categories():
    mycursor.execute('SELECT id, category_name FROM categories ORDER BY id')
    categories = mycursor.fetchall()     
    for item in categories:
        print('{} - {}'.format(item[0], item[1]))

    #select category
    while True:
        choice = input("Selectionnez l'id d'une categorie\n \nVotre choix: ")
        try:
            if int(choice) > len(categories):
                print("Veuillez entrer un numero correspondant a une categorie")
            else:
                break
        except ValueError:
            print("Veuillez entrer un numero correspondant a une categorie")
    sql = " SELECT * FROM foods WHERE category_id = %s ORDER BY id"
    val = [choice]
    mycursor.execute(sql, val)
    foods = mycursor.fetchall()
    for item in foods:
        print('{} - {}'.format(item[0], item[1]))

    #select food
    while True:
        selected_food_id = input("Selectionnez un aliment à substituer\n \nVotre choix: ")
        try: 
            if int(selected_food_id) > foods[len(foods)-1][0] or int(selected_food_id) < foods[0][0]:
                print("Veuillez entrer un numero correspondant a un aliment")
            else:
                break
        except:
            print("Veuillez entrer un numero")
    sql = 'SELECT nova_group FROM foods WHERE id = %s'
    val = [selected_food_id]
    mycursor.execute(sql, val)
    nutriscore = mycursor.fetchall()
    find_substitute = "SELECT * FROM foods WHERE nova_group < %s AND category_id = %s ORDER BY RAND() LIMIT 1"
    val = [(nutriscore[0][0], choice[0][0])]
    mycursor.executemany(find_substitute, val)
    substitute = mycursor.fetchall()

    #display substitute
    if len(substitute) == 0: 
        print("Ce produit est l'un des plus sain de cette catégorie") 
    else:
        sql = ' SELECT stores_id FROM foods_stores WHERE foods_id = %s '
        val = [(substitute[0][0],)]
        mycursor.executemany(sql, val)
        stores_id = mycursor.fetchall()
        sql = 'SELECT product_name FROM foods WHERE id = %s'
        val = [(selected_food_id,)]
        mycursor.executemany(sql,val)
        selected_food = mycursor.fetchall()
        print("Vous avez séléctionné: {}\n"
            "Cet aliment a un nutriscore de: {}\n"
            "\nVoici un aliment plus sain de la même catégorie:\n"
            "Nom: {}\n"
            "Nutriscore: {}\n"
            "Page OpenFoodFact: {}\n"
            .format(selected_food[0][0], nutriscore[0][0], substitute[0][1], substitute[0][2], substitute[0][4]))
        if len(stores_id) != 0:
            print("Ou l'acheter:")
            for store_id in stores_id:
                sql = 'SELECT * FROM stores WHERE id = %s'
                val = [(store_id[0],)]
                mycursor.executemany(sql, val)
                stores_name = mycursor.fetchall()
                print(stores_name[0][1])

        #Save substitute
        save = input("Voulez vous sauvegarder cet aliment de substitution ? [Y/N]")
        if save.upper() == "Y":
            sql = 'SELECT id FROM foods WHERE product_name = %s'
            val = [(substitute[0][1],)]
            mycursor.executemany(sql,val)
            foods_subs_id = mycursor.fetchall()
            sql = "INSERT IGNORE INTO favorites (foods_id, foods_subs_id) VALUES (%s, %s)" #we add ignore in case of a duplicate
            val = (selected_food_id, foods_subs_id[0][0])
            mycursor.execute(sql, val)
            mydb.commit()
            print("élément sauvegardé !")
        else:
            print("Bonne journée !")
        
#Show favorites
def display_saved_food():
    mycursor.execute("SELECT foods_subs_id, foods_id FROM favorites")
    fav_id_list = mycursor.fetchall()
    for item in fav_id_list:
        sql = 'SELECT product_name FROM foods WHERE id = %s'
        val = [(item[0],)]
        mycursor.executemany(sql, val)
        foods_subs_name = mycursor.fetchall()
        sql = 'SELECT product_name FROM foods WHERE id = %s'
        val = [(item[1],)]
        mycursor.executemany(sql, val)
        foods_id_name = mycursor.fetchall()
        print(" - {} (remplace l'aliment: {})".format(foods_subs_name[0][0] , foods_id_name[0][0]))


display_terminal()