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
    "\n Votre choix: \n")
    if choice == "1":
        display_categories()
    else: 
        print("en chantier")
        
# This function display the categories
def display_categories():
    mycursor.execute("SHOW TABLES")
    categories = mycursor.fetchall() 
    liste_categories = []
    for x in categories:
        liste_categories.append(x)     # for some reason this doesnt simply add the table " boissons " but a tuple: " ('boisson',) "
    for item in enumerate(liste_categories):
        print(item)
    choice = input("Selectionnez une catégorie\n Votre choix: ")
    sql = " SELECT Product_name AS Aliment FROM " + liste_categories[int(choice)][0]
    mycursor.execute(sql)
    product_names = mycursor.fetchall()
    for y in (product_names):
        print(y)                   # meme probleme que plus haut, ca renvoie des tuples et non simplement le nom des aliments



        




