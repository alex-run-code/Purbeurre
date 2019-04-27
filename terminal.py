import mysql.connector

# Initializing database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="210991"
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
    choice = input("Selectionnez l'id d'une categorie\n \nVotre choix: ")
    sql = " SELECT * FROM foods WHERE category_id = '" + choice + "' ORDER BY id"
    mycursor.execute(sql)
    foods = mycursor.fetchall()
    for item in foods:
        print('{} - {}'.format(item[0], item[1]))

    #select food
    selected_food_id = input("Selectionnez un aliment à substituer\n \nVotre choix: ")
    selected_food_id = str(selected_food_id)
    find_nutriscore = "SELECT nova_group FROM foods WHERE id = '" + selected_food_id + "'"
    mycursor.execute(find_nutriscore)
    nutriscore = mycursor.fetchall()
    nustriscore = str(nutriscore[0][0])
    find_substitute = "SELECT * FROM foods WHERE nova_group < " + nustriscore + " AND category_id = '" + choice + "' ORDER BY RAND() LIMIT 1"
    mycursor.execute(find_substitute)
    substitute = mycursor.fetchall()

    #display substitute
    if len(substitute) == 0: 
        print("Ce produit est l'un des plus sain de cette catégorie") 
    else:
        mycursor.execute("SELECT stores_id FROM foods_stores WHERE foods_id = " + str(substitute[0][0]))
        stores_id = mycursor.fetchall()
        mycursor.execute("SELECT product_name FROM foods WHERE id = '" + str(selected_food_id) + "'")
        selected_food = mycursor.fetchall()
        print("Vous avez séléctionné: {}\n"
            "Cet aliment a un nutriscore de: {}\n"
            "\nVoici un aliment plus sain de la même catégorie:\n"
            "Nom: {}\n"
            "Nutriscore: {}\n"
            "Page OpenFoodFact: {}\n"
            .format(selected_food[0][0], nustriscore, substitute[0][1], substitute[0][2], substitute[0][4]))
        if len(stores_id) != 0:
            print("Ou l'acheter:")
            for store_id in stores_id:
                mycursor.execute("SELECT * FROM stores WHERE id = " + str(store_id[0]))
                stores_name = mycursor.fetchall()
                print(stores_name[0][1])

        #Save substitute
        save = input("Voulez vous sauvegarder cet aliment de substitution ? [Y/N]")
        if save.upper() == "Y":
            mycursor.execute("SELECT id FROM foods WHERE product_name = '" + str(substitute[0][1]) + "'")
            foods_subs_id = mycursor.fetchall()
            sql = "INSERT INTO favorites (foods_id, foods_subs_id) VALUES (%s, %s)"
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
        mycursor.execute("SELECT product_name FROM foods WHERE id = " + str(item[0]))
        foods_subs_name = mycursor.fetchall()
        mycursor.execute("SELECT product_name FROM foods WHERE id = " + str(item[1]))
        foods_id_name = mycursor.fetchall()
        print(" - {} (remplace l'aliment: {})".format(foods_subs_name[0][0] , foods_id_name[0][0]))
    #saved_food = mycursor.fetchall()
    #for food in saved_food:
        #print(food)


display_terminal()