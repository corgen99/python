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

# def selection_ligne(ligne):
#     def controle_nombre():
#         def compte_nombre(nombre):
#             count=0
#             for i in range(9):
#                 if nombre in ligne[i]:
#                     count+=1
#             return count
#         controle=[]
#         for i in range(1,10):
#             controle.append(compte_nombre(i))
#         return controle
         
#     def recherche_uniques():
#         '''
#         Recherche des nombres seuls et les retire des autres sous-chaines
#         '''
#         def retirer_valeur(valeur,indice):
#             """
#             recherche les autres occurences de la valeur dans la liste
#             """
#             for j in range(9): #on balaye toutes les sous-listes
#                 if j!=indice and valeur in ligne[j]: #si la valeur est dans la ligne de j et que j n'est pas l'indice recherché
#                     ligne[j].remove(valeur)
#                     if len(ligne[j])==1:
#                         cases_a_traiter.append(j)
        
#         for i in cases_a_traiter: #on balaye les cases à traiter
#             cases_a_traiter.remove(i)
#             case_traitee.append(i)
#             retirer_valeur(ligne[i], i)
    
#     # compte le nombre d'occurrence de chaque nombre dans les différentes sous-listes, pour s'assurer qu'il n'y en a pas un qui est le dernier disponible
#     compte=controle_nombre()

#     # les cases a traiter en priorité sont celles ou une seule valeur est disponible
#     cases_a_traiter=[i for i in range(9) if len(ligne[i])==1]
#     case_traitee=[]
    
#     # on initialise en cherchant les nombres uniques dans leur ligne ayant pas encore été traités
#     recherche_uniques()
#     for i in range(9):
#         if i not in case_traitee: #si la case n'est pas traitée
#             random.shuffle(ligne[i])
#             ligne[i]=[ligne[i].pop()]
#             cases_a_traiter.append(i)
#             recherche_uniques()
    
#     return ligne



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
    for i in range(len(ligne)):
        for j in range(len(ligne[i])):
            res[ligne[i][j]-1]+=1
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
                valeurs_traites.append(ligne[i]) #on indique que la valeur est traitée
                retirer_valeurs(ligne,ligne[i])
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
    # print(ligne)
    ligne=creation_ligne(ligne)
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
            grille=placer_nombre(grille,nouvelle_ligne[j],i,j)
    
    return grille