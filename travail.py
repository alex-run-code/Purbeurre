
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
recherche = openfoodfacts.products.get_product("26038681")
print(recherche)


import openfoodfacts

#add all the food with needed data in a list
def add_food_in_list(category):
    products = openfoodfacts.products.get_by_facets({
    'category': category,
    'language': 'france'
    })
    list_of_food = []
    for food in products:
        rules = ['product_name_fr' in food,
                'nova_group' in food,
                'countries_tags' in food,
                'stores_tags' in food,
                ]
        if all(rules):
            list_of_food.append([
                {'product_name' : food['product_name']},
                {'nova_group' : food['nova_group']},
                {'countries_tags' : food['countries_tags']},
                {'stores_tags' : food['stores_tags']},
                ])
            print("added successfully")
    
    return list_of_food

# mes listes
list_of_snacks = add_food_in_list('snacks')
list_of_boissons = add_food_in_list('boissons')
list_of_viandes = add_food_in_list('viandes')
list_of_charcuteries = add_food_in_list('charcuteries')
list_of_desserts = add_food_in_list('desserts')
        

# liste les noms des produits d'une liste
for item in list_of_snacks:
    for data in item:
        if 'product_name' in data:
            print(data['product_name'])


# Si on execute cette recherche, on ne trouvera pas le produit " sarialis " dans la liste.
# Alors que, sur le site, si on cherche dans les snacks français, on trouve bien Sarialis. 

def test_rapide(category):
    products = openfoodfacts.products.get_by_facets({
    'category': category,
    'language': 'france'
    })
    for item in products:
        for data in item:
            print(data)

test_rapide('snacks')

######

def recherche_categorie(category):
    products = openfoodfacts.products.get_by_facets({
    'category': category,
    'language': 'france'
    })
    for item in products:
        if 'energy_value' in item['nutriments']:
            print(item['nutriments']['energy_value'])



recherche_categorie('boissons')