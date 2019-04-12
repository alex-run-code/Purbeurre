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
    print("nutriscore is", nutriscore[0][0])
    nustriscore = str(nutriscore[0][0])
    find_substitute = "SELECT * FROM " + categories[choice][0] + " WHERE nova_group < " + nustriscore + " ORDER BY RAND() LIMIT 1"
    mycursor.execute(find_substitute)
    substitute = mycursor.fetchall()
    print(substitute)








display_terminal()