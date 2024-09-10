def recherche(liste, valeur):
    return [i for i in range(len(liste)) if liste[i] == valeur]

liste=[1,2,3,4,1,2,5,6,1,3,4,8,1,9,3,2,6,7,4,1,2]
valeur=3

print(recherche(liste,valeur))