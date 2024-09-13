'''
affichage des fonctions
'''

def ajouter_ligne_trait():
    for j in range(49):
        print("-", end="",sep="")
    print()

def print_belle_grille(grille):
    '''
    affiche une grille donnée en entrée
    '''
    for i in range(9):
        if i%3==0:
            ajouter_ligne_trait()
        
        for j in range(3):
            if j==0 :
                print("| ", end="", sep="")
            print("[",grille[i][3*j],",",grille[i][3*j+1],",",grille[i][3*j+2],"] | ",end="")
        print()

    ajouter_ligne_trait()

def print_grille_simple(grille):
    for i in range(9):
        print(grille[i])
    print()