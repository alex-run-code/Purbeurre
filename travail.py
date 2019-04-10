
import openfoodfacts
import random

categories = openfoodfacts.facets.get_categories()
categories_fr = []
products = openfoodfacts.products.get_by_category("sodas")


def main_loop(): # Opening Script
    print("Selectionnez un menu \n"
    "1- Voir la liste des catégories \n"
    "2- Voir mes aliments substitués \n")
    choice = input("\n Votre choix: \n")
    if choice == "1":
        category_list_fr()
    else: 
        print("en chantier")

def category_list_fr(): # Display all french categories and add them in 'categories_fr'
    i = 1
    for food in categories:
        if "fr" in food['name']:
            print("{}: {}".format(i, food['name']))
            categories_fr.append(food)
            i = i+1

def substitute():
    substitute_number = int(input("Selectionnez un élément: "))
    substitute_name = categories_fr[substitute_number - 1]['name']
    substitute_list = openfoodfacts.products.get_by_category(substitute_name)
    rand_sub = random.choice(substitute_list)
    print(rand_sub)
    

main_loop()

def category_count(): # Display all french categories and add them in 'categories_fr'
    for food in categories:
        if "fr" in food['name']:
            cat_size = len(openfoodfacts.products.get_by_category(food['name']))
            print(food['name'])
            print(cat_size)


display_food = openfoodfacts.products.get_by_category("Wines from France")

search = openfoodfacts.products.get_product("3700214617724")



list_of_snacks = []
list_of_boissons = []
list_of_viandes = []
list_of_Charcuteries = []
list_of_Desserts = []




#add all the food with needed data in list "list_snacks"
def add_food_in_category(category):
    products = openfoodfacts.products.get_by_category(category)
    for food in products:
        rules = ['product_name' in food,
                'nova_group' in food,
                'countries_tags' in food,
                'ingredients_text_fr' in food,
                'stores_tags' in food,
                ]
        if all(rules):
            list_of_snacks.append([
                {'product_name' : food['product_name']},
                {'nova_group' : food['nova_group']},
                {'countries_tags' : food['countries_tags']},
                {'ingredients_text_fr' : food['ingredients_text_fr']},
                {'stores_tags' : food['stores_tags']},
            ])
            print("added successfully")

        
 