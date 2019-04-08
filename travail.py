
import openfoodfacts


categories = openfoodfacts.facets.get_categories()
categories_20 = []

def list_categ():
    i = 1
    for dico in categories:
        if i <= 20:
            categories_20.append(dico['name'])
            print("{}: {}".format(i, dico['name']))
            i = i+1
        else:
            break

def main_loop():
    choix = input(
        "Que voulez vous faire ? \n"
        "1- Substituer un aliment \n"
        "2- Voir mes aliments substitués \n"
            )

    if choix == "1":
        list_categ(10)
    elif choix == "2":
            print("en cours")
    else:
        print("echec")

list_categ()
print(categories_20)



