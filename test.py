# tests
#installé openfoodfacts avec python -m pip install openfoodfacts


dico1 = {
    'nom': 'cambefort', 
    'prenom': 'alexandre'
    }

dico2 = {
'nom': 'cambefort', 
'prenom': 'bertrand'
}

dico3 = {
'nom': 'cambefort', 
'prenom': 'nathalie'
}
    
liste = [
    dico1, 
    dico2, 
    dico3]

for dico in liste:
    if "nom" in dico:
        print("Nom est dans {}".format(dico))


liste1 = ["a","b","c"]
liste2 = [""]
liste3 = []

dicoa = {'name':"alex"}
dicob = {'name':[]}
print(len(dicob['name']))