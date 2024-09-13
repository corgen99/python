def nouvelle_grille():
    '''
    créée une nouvelle grille vierge de sudoku
    '''
    return 9*[9*[0]]

def print_belle_grille(grille):
    '''
    affiche une grille donnée en entrée
    '''
    for i in range(9):
        if i%3==0:
            for j in range(49):
                print("-", end="",sep="")
            print()

        for j in range(3):
            if j==0 :
                print("| ", end="", sep="")
            print("[",grille[i][3*j],",",grille[i][3*j+1],",",grille[i][3*j+2],"] | ",end="")
        print()
    for j in range(49):
        print("-", end="",sep="")
    print()

def print_grille_simple(grille):
    for i in range(9):
        print(grille[i])
    print()

def placer_nombre(grille,chiffre,ligne,colonne):
    '''
    place le nombre voulu dans la ligne et la colonne indiquée
    on suppose que le chiffre est entre 
    '''
    grille[ligne][colonne]=chiffre
    return grille

grille_test=nouvelle_grille()
print_grille_simple(grille_test)

grille_test=placer_nombre(grille_test, 3, 2, 1)
print_grille_simple(grille_test)