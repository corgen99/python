'''
creation d'une nouvelle grille aleatoire
'''
import random
from verification import *
from gameplay import placer_nombre, nombres_carre, nombres_ligne, nombres_colonne
from affichage import print_belle_grille

def nouvelle_grille():
    '''
    créée une nouvelle grille vierge de sudoku
    '''
    grille=[]
    for i in range(9):
        grille.append([])
        for j in range(9):
            grille[i].append(0)
    return grille

def nombre_aleatoire():
    return random.randint(1,9)

def nombres_dispo(grille, ligne_actuelle, numero_ligne, numero_colonne):
    '''
    renvoie les nombres disponibles
    '''
    colonne=nombres_colonne(grille, numero_colonne)
    ligne=nombres_ligne(grille, numero_ligne)
    carre=nombres_carre(grille, (numero_ligne//3)*3+numero_colonne//3)
    liste=colonne+ligne+carre+ligne_actuelle

    liste_dispo=[]
    for i in range(1,10):
        if i not in liste:
            liste_dispo.append(i)
    return liste_dispo

def nombres_dispo(grille, numero_ligne, numero_colonne):
    '''
    renvoie les nombres disponibles
    '''
    if grille[numero_ligne][numero_colonne]:
        return [grille[numero_ligne][numero_colonne]]
    
    colonne=nombres_colonne(grille, numero_colonne)
    ligne=nombres_ligne(grille, numero_ligne)
    carre=nombres_carre(grille, (numero_ligne//3)*3+numero_colonne//3)
    liste=colonne+ligne+carre

    liste_dispo=[]
    for i in range(1,10):
        if i not in liste:
            liste_dispo.append(i)
    return liste_dispo

def valeurs_dispo_ligne(grille, numero_ligne):
    '''
    renvoie la liste des valeurs dispo pour toutes les lignes
    '''
    res=[]
    for i in range(9):
        disponibles=nombres_dispo(grille, numero_ligne, i)
        res.append(disponibles)
    return res

def nouveau_nombre(grille, ligne_actuelle, numero_ligne, numero_colonne):
    '''
    trouve un nouveau nombre répondant aux contraintes
    '''
    if grille[numero_ligne][numero_colonne] != 0:
        return grille[numero_ligne][numero_colonne]
    else:
        liste_nombres=nombres_dispo(grille, ligne_actuelle, numero_ligne, numero_colonne)
        random.shuffle(liste_nombres)
        print(liste_nombres)
        return liste_nombres[0]
        

def creer_ligne(grille, numero_ligne):
    '''
    crée la ligne demandée
    '''
    ligne=[]
    for i in range(9):
        ligne.append(nouveau_nombre(grille, ligne, numero_ligne, i))
        print(f"Ligne {numero_ligne}, valeur : {ligne}")
    return ligne

# def creer_colonne(grille,numero_colonne):
#     '''
#     crée la colonne demandée
#     '''
#     colonne=[]
#     for i in range(9):
#         colonne.append(nouveau_nombre(grille, i, numero_colonne))
#     return colonne

def creer_grille():
    '''
    creation d'une grille
    '''
    grille=nouvelle_grille()
    premier_bloc=[1,2,3,4,5,6,7,8,9]
    random.shuffle(premier_bloc)
    for i in range(9):
        grille=placer_nombre(grille,premier_bloc[i],i//3,i%3)
    
    print_belle_grille(grille)
    for i in range(9):
        # nouvelle_ligne=creer_ligne(grille,i)
        # for j in range(9):
        #     grille=placer_nombre(grille,nouvelle_ligne[j],i,j)
        print(f"Ligne {i}, valeurs disponibles : {valeurs_dispo_ligne(grille, i)}")
    
    return grille