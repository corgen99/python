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

def rechercher_uniques(ligne):
    """
    recherche les cases contenant une seule valeur
    """
    return [i for i in range(len(ligne)) if len(ligne[i])==1]

def compte_nombre(ligne):
    """
    compte le nombre d'occurrence de chaque nombre dans une ligne donnée
    """
    res=[0]*9
    for sous_ligne in ligne:
        for valeur in sous_ligne:
            res[valeur-1]+=1
    return res

def rechercher_nombre_unique(ligne):
    """
    recherche les nombres n'apparaissant que dans une case
    """
    compte=compte_nombre(ligne)
    return [i+1 for i in range(len(ligne)) if compte[i]==1]
    
def valeur_aleatoire(sous_ligne):
    """
    prend une valeur aléatoire dans une sous-ligne
    """
    random.shuffle(sous_ligne)
    return sous_ligne.pop()

def retirer_valeurs(ligne,valeur):
    for sous_ligne in ligne:
        if len(sous_ligne)>1 and valeur in sous_ligne:
            sous_ligne.remove(valeur)
    return ligne

def chercher(ligne, valeur):
    for i in range(len(ligne)):
        if valeur in ligne[i]:
            return i
    return -1

def creation_ligne(ligne):
    """
    crée une ligne à partir d'une liste contenant la liste des valeurs disponibles pour chaque case
    """
    liste=[0]*9
    valeurs_traites=[]
    cases_traitees=[]
    traitement=True

    while len(cases_traitees)!=len(ligne) and traitement: #Itérer tant qu'on n'a pas traité toutes les cases
        traitement=False
        cases_uniques=rechercher_uniques(ligne)
        for i in cases_uniques:
            if i not in cases_traitees: #on la traite
                cases_traitees.append(i) #on indique que la case est traitée
                valeurs_traites.append(ligne[i][0]) #on indique que la valeur est traitée
                retirer_valeurs(ligne,ligne[i][0])
                liste[i]=ligne[i][0]
                traitement=True
        
        valeurs_uniques=rechercher_nombre_unique(ligne)
        for i in valeurs_uniques:
            if i not in valeurs_traites: #on la traite
                case_a_traiter=chercher(ligne,i)
                cases_traitees.append(case_a_traiter)
                valeurs_traites.append(i)
                ligne[case_a_traiter]=[i]
                liste[case_a_traiter]=i
                retirer_valeurs(ligne,i)
                traitement=True
        
        if not traitement:
            for i in range(len(ligne)):
                if i not in cases_traitees and not traitement:
                    valeur=valeur_aleatoire(ligne[i])
                    cases_traitees.append(i)
                    valeurs_traites.append(valeur)
                    ligne[i]=[valeur]
                    liste[i]=valeur
                    retirer_valeurs(ligne,valeur)
                    traitement=True
        
    return liste
    
def creer_ligne(grille, numero_ligne):
    '''
    crée la ligne demandée
    '''
    ligne=valeurs_dispo_ligne(grille,numero_ligne)
    ligne=creation_ligne(ligne)
    return ligne

def init_grille():
    grille=nouvelle_grille()
    premier_bloc=[1,2,3,4,5,6,7,8,9]
    random.shuffle(premier_bloc)
    for i in range(9):
        grille=placer_nombre(grille,premier_bloc[i],i//3,i%3)
    return grille

def creer_grille():
    '''
    creation d'une grille
    '''
    grille=init_grille()
    
    while True:
        try:
            for i in range(9):
                nouvelle_ligne=creer_ligne(grille,i)
                for j in range(9):
                    grille=placer_nombre(grille,nouvelle_ligne[j],i,j)
        except:
            grille=init_grille()
            continue
        break
    return grille


def selection_positions(nombre_indices):
    pos_indices=[]
    for i in range(nombre_indices):
        pos=-1
        while pos in pos_indices or pos<0:
            pos=random.randint(0,80)
        pos_indices.append(pos)
    return pos_indices

def effacer(grille, ligne, colonne):
    grille[ligne][colonne]=0
    return grille

def effacer_position(grille,position,pos_indices):
    if position in pos_indices:
        return grille
    else:
        ligne=position//9
        colonne=position%9
        return effacer(grille,ligne,colonne)

def blanchir_grille(grille):
    nombre_indices=random.randint(25,30)
    pos_indices=selection_positions(nombre_indices)
    for i in range(81):
        grille=effacer_position(grille, i, pos_indices)
    return grille

def generer_grille():
    grille=creer_grille()
    return blanchir_grille(grille)