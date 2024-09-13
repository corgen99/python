def verifier_ligne(grille, ligne):
    ligne_extraite=[]
    for i in range(9):
        ligne_extraite.append(grille[ligne][i])
    ligne_extraite.sort()
    return ligne_extraite==[1,2,3,4,5,6,7,8,9]

def verifier_colonne(grille, colonne):
    colonne_extraite=[]
    for i in range(9):
        colonne_extraite.append(grille[i][colonne])
    colonne_extraite.sort()
    return colonne_extraite==[1,2,3,4,5,6,7,8,9]
    
def verifier_carre(grille,carre):
    carre_extrait=[]
    for i in range(3):
        for j in range(3):
            carre_extrait.append(grille[(carre//3)*3+i][(carre%3)*3+j])
    carre_extrait.sort()
    return carre_extrait==[1,2,3,4,5,6,7,8,9]

def verifier_grille(grille):
    '''
    verifie si une grille est correcte ou non
    '''
    for i in range(9):
        if not verifier_ligne(grille,i) or not verifier_colonne(grille,i) or not verifier_carre(grille,i):
            return False
    return True