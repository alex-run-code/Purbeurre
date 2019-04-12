import openfoodfacts
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
    choice = input ("Selectionnez un menu \n"
    "1- Voir la liste des catégories \n"
    "2- Voir mes aliments substitués \n"
    "\nVotre choix: ")
    if choice == "1":
        display_categories()
    else: 
        print("en chantier")
        
# This function display the categories
def display_categories():
    mycursor.execute("SHOW TABLES")
    categories = mycursor.fetchall()     # for some reason this doesnt simply add the table " boissons " but a tuple: " ('boisson',) "
    for i, item in enumerate(categories):
        print(i+1,"-",item[0])
    choice = input("Selectionnez une catégorie\n \nVotre choix: ")
    choice = int(choice) - 1
    sql = " SELECT Product_name AS Aliment FROM " + categories[choice][0]
    mycursor.execute(sql)
    product_names = mycursor.fetchall()
    for i, item in enumerate(product_names):
        print(i+1, "-", item[0])           # meme probleme que plus haut, ca renvoie des tuples et non simplement le nom des aliments
    selected_food = input("Selectionnez un aliment à substituer\n \nVotre choix: ")
    selected_food = int(selected_food)
    find_nutriscore = "SELECT nova_group FROM " + categories[choice][0] + " WHERE id =" + str(selected_food)
    mycursor.execute(find_nutriscore)
    nutriscore = mycursor.fetchall()
    nustriscore = str(nutriscore[0][0])
    find_substitute = "SELECT * FROM " + categories[choice][0] + " WHERE nova_group < " + nustriscore + " ORDER BY RAND() LIMIT 1"
    mycursor.execute(find_substitute)
    substitute = mycursor.fetchall()
    if len(substitute) == 0: 
        print("Ce produit est l'un des plus sain de cette catégorie") 
    else:
        stores = substitute[0][4]
        print("Vous avez séléctionné: {}\n"
            "Cet aliment a un nutriscore de: {}\n"
            "\nVoici un aliment plus sain de la même catégorie:\n"
            "Nom: {}\n"
            "Nutriscore: {}"
            .format(product_names[selected_food][0], nustriscore, substitute[0][1], substitute[0][2]))
        if len(stores) != 2:
            print("Où l'acheter: {}\n".format(stores))
        save = input("Voulez vous sauvegarder cet aliment de substitution ? [Y/N]")
        if save.upper() == "Y":
            nom_aliment = str(substitute[0][1])
            sql = "INSERT INTO sauvegarde (Product_name) VALUES (%s)"
            val = (nom_aliment,)
            mycursor.execute(sql, val)
            mydb.commit()
            print("élément sauvegardé !")
        else:
            print("Bonne journée !")
        

    






display_terminal()