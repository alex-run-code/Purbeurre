
import openfoodfacts
import random

categories = openfoodfacts.facets.get_categories()
categories_fr = []


products = openfoodfacts.products.get_by_category("fr:gaufres-sucrees")

def category_list_fr():
    i = 1
    for food in categories:
        if "fr" in food['name']:
            print("{}: {}".format(i, food['name']))
            categories_fr.append(food)
            i = i+1

def substitute():
    substitute_number = input("Selectionnez un élément: ")
    substitute_number = int(substitute_number)
    substitute_name = categories_fr[substitute_number - 1]['name']

    substitute_number
    substitute_list = openfoodfacts.products.get_by_category(substitute_name)
    rand_sub = random.choice(substitute_list)
    print(rand_sub)

def main_loop():
    choix = input(
        "Que voulez vous faire ? \n"
        "1- Substituer un aliment \n"
        "2- Voir mes aliments substitués \n"
            )

    if choix == "1":
        category_list_fr()
        substitute()
    elif choix == "2":
            print("en cours")
    else:
        print("echec")


main_loop()

