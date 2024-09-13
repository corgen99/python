'''
ajout d'un nombre dans une grille
boucle principale du jeu
'''

from verification import verifier_grille
from affichage import *

def placer_nombre(grille,chiffre,ligne,colonne):
    '''
    place le nombre voulu dans la ligne et la colonne indiquée
    on suppose que le chiffre est entre 
    '''
    grille[ligne][colonne]=chiffre
    return grille

def nombres_ligne(grille, ligne):
    '''
    renvoie les nombres dans une ligne donnée
    '''
    res=[]
    for i in range(9):
        if grille[ligne][i]>0:
            res.append(grille[ligne][i])
    return res

def nombres_colonne(grille,colonne):
    '''
    renvoie les nombres dans une colonne donnée
    '''
    res=[]
    for i in range(9):
        if grille[i][colonne]>0:
            res.append(grille[i][colonne])
    return res

def nombres_carre(grille,carre):
    '''
    renvoie les nombres présents dans le carré donné
    '''
    res=[]
    for i in range(3):
        for j in range(3):
            if grille[(carre//3)*3+i][(carre%3)*3+j]>0:
                res.append(grille[(carre//3)*3+i][(carre%3)*3+j])
    return res

def chercher_valeurs_possible(grille, ligne, colonne):
    '''
    cherche les valeurs possibles d'une case donnée
    '''
    numero_carre=3*(ligne//3)+(colonne//3)
    nombres_indisponible=nombres_ligne(grille,ligne)+nombres_colonne(grille,colonne)+nombres_carre(grille,numero_carre)
    return [i for i in range(1,10) if i not in nombres_indisponible ]

def resoudre(grille):
    stagnation=False
    while not verifier_grille(grille) and not stagnation:
        stagnation += 1
        for i in range(9):
            for j in range(9):
                if grille[i][j]==0:
                    valeurs_possibles=chercher_valeurs_possible(grille,i,j)
                    if len(valeurs_possibles)==1:
                        placer_nombre(grille,valeurs_possibles[0],i,j)
                        stagnation=False
    return grille