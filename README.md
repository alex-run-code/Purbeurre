# Purbeurre

# dbfiller.py

Ce programme sert à remplir la base de donner. 

## add_food_in_db(category)

Cette fonction ajoute la liste des aliments de la catégorie choisie dans la base de donnée. 

## add_category_in_db(category)

Cette fonction ajoute la catégorie choisie dans la base de donnée.

## fill_categories()

Cette fonction ajoute une liste de catégorie pré-définies dans la base de donnée. 

## fill_foods()

Cette fonction ajoute les aliments appartenant aux catégories choisies dans la base de donnée. 

# purbeurre.py

Il s'agit du programme principal

## display_terminal()

Cette fonction affiche le terminal avec lequel l'utilisateur va interagir 

### display_terminal - select category

Il est d'abord demandé à l'utilisation de selectionner une catégorie

### display_terminal - select category

L'utilisateur choisi ensuite un aliment

### display_terminal - display substitute

Si le programme trouve un aliment plus sain dans la base de donnée, il est proposé à l'utilisateur. 

### display_terminal - Save substitute

Le programme propose enfin à l'utilisateur de sauvegardé le substitue.

## display_saved_food()

Cette fonction affiche la liste d'éléments sauvegardés
