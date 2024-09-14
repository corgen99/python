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

def nombres_dispos(grille, ligne_actuelle, numero_ligne, numero_colonne):
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

# def nouveau_nombre(grille, ligne_actuelle, numero_ligne, numero_colonne):
#     '''
#     trouve un nouveau nombre répondant aux contraintes
#     '''
#     if grille[numero_ligne][numero_colonne] != 0:
#         return grille[numero_ligne][numero_colonne]
#     else:
#         liste_nombres=nombres_dispos(grille, ligne_actuelle, numero_ligne, numero_colonne)
#         random.shuffle(liste_nombres)
#         return liste_nombres[0]

def selection_ligne(ligne):
    def controle_nombre():
        def compte_nombre(nombre):
            count=0
            for i in range(9):
                if nombre in ligne[i]:
                    count+=1
            return count
        controle=[]
        for i in range(1,10):
            controle.append(compte_nombre(i))
        return controle
    
    def nombres_a_traiter():
        return [i for i in range(9) if compte[i]>1]
     
    def recherche_uniques():
        '''
        Recherche des nombres seuls et les retire des autres sous-chaines
        '''
        def retirer_valeur(valeur,indice):
            """
            recherche les autres occurences de la valeur dans la liste
            """
            for j in range(9): #on balaye toutes les sous-listes
                if j!=indice and valeur in ligne[j]: #si la valeur est dans la ligne de j et que j n'est pas l'indice recherché
                    ligne[j].remove(valeur)
                    compte[valeur-1]-=1

        for i in range(9): #on balaye les sous-listes
            if len(ligne[i])==1 and not traite[ligne[i]-1]: #si la sous liste est de taille 1 et que le nombre dedans n'a pas été traité
                traite[ligne[i]-1]=True #on signale qu'on l'a traité
                retirer_valeur(ligne[i], i)
    
    traite=[]
    for i in range(9):
        traite.append(False)

    compte=controle_nombre()
    traite=nombres_a_traiter()

    
    recherche_uniques()
    for i in range(9):
        if len(ligne[i])>1:
            random.shuffle(ligne[i])
            ligne[i]=[ligne[i].pop()]
            recherche_uniques()
    
    return ligne

[4,8,2,9,6,3,7,1,5]

def creer_ligne(grille, numero_ligne):
    '''
    crée la ligne demandée
    '''
    ligne=valeurs_dispo_ligne(grille,numero_ligne)
    print(ligne)
    ligne=selection_ligne(ligne)
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
        print(f"Traitement de la ligne {i}")
        print("Grille :")
        print_belle_grille(grille)
        nouvelle_ligne=creer_ligne(grille,i)
        print(f"Nouvelle ligne : {nouvelle_ligne}")
        for j in range(9):
            grille=placer_nombre(grille,nouvelle_ligne[j][0],i,j)
    
    return grille