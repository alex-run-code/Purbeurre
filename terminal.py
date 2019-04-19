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
    mycursor.execute('SELECT category_name FROM categories')
    categories = mycursor.fetchall()     
    for i, item in enumerate(categories):
        print(i+1,"-",item[0])

    #select category
    choice = input("Selectionnez une catégorie\n \nVotre choix: ")
    choice = int(choice) - 1
    sql = " SELECT Product_name AS Aliment FROM foods WHERE category_name = '" + str(categories[choice][0]) + "'"
    mycursor.execute(sql)
    product_names = mycursor.fetchall()
    for i, item in enumerate(product_names):
        print(i+1, "-", item[0])          

    #select food
    selected_food = input("Selectionnez un aliment à substituer\n \nVotre choix: ")
    selected_food = int(selected_food)
    find_nutriscore = "SELECT nova_group FROM foods WHERE Product_name = '" + str(product_names[selected_food][0]) + "'"
    mycursor.execute(find_nutriscore)
    nutriscore = mycursor.fetchall()
    nustriscore = str(nutriscore[0][0])
    find_substitute = "SELECT * FROM foods WHERE nova_group < " + nustriscore + " ORDER BY RAND() LIMIT 1"
    mycursor.execute(find_substitute)
    substitute = mycursor.fetchall()

    #display substitute
    if len(substitute) == 0: 
        print("Ce produit est l'un des plus sain de cette catégorie") 
    else:
        stores = substitute[0][5]
        print("Vous avez séléctionné: {}\n"
            "Cet aliment a un nutriscore de: {}\n"
            "\nVoici un aliment plus sain de la même catégorie:\n"
            "Nom: {}\n"
            "Nutriscore: {}\n"
            "Page OpenFoodFact: {}"
            .format(product_names[selected_food][0], nustriscore, substitute[0][1], substitute[0][2], substitute[0][6]))
        if len(stores) != 2:
            print("Où l'acheter: {}\n".format(stores))

        #Save substitute
        save = input("Voulez vous sauvegarder cet aliment de substitution ? [Y/N]")
        if save.upper() == "Y":
            nom_aliment = str(substitute[0][1])
            sql = "INSERT INTO favorites (Product_name) VALUES (%s)"
            val = (nom_aliment,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("élément sauvegardé !")
        else:
            print("Bonne journée !")
        
#Show favorites
def display_saved_food():
    mycursor.execute("SELECT Product_name FROM favorites")
    saved_food = mycursor.fetchall()
    for food in saved_food:
        print(food[0])


display_terminal()