'''
creation d'une nouvelle grille aleatoire
'''

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