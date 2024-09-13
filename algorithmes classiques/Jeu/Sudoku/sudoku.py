from affichage import *
from verification import verifier_grille

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


def placer_nombre(grille,chiffre,ligne,colonne):
    '''
    place le nombre voulu dans la ligne et la colonne indiquée
    on suppose que le chiffre est entre 
    '''
    grille[ligne][colonne]=chiffre
    return grille

