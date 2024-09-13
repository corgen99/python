from sudoku import *

def test_ajouter_nombre():
    valeur=4
    ligne=2
    colonne=3
    grille=nouvelle_grille()
    grille=placer_nombre(grille, valeur, ligne, colonne)

    expected_value=[\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,4,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0,0]]

    assert grille==expected_value

def test_verifier_ligne_correcte():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    ligne=4
    expected_value=True
    assert verifier_ligne(grille,ligne)==expected_value

def test_verifier_ligne_incorrecte():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [2,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    ligne=4
    expected_value=False
    assert verifier_ligne(grille,ligne)==expected_value

def test_verifier_colonne_correcte():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    colonne=4
    expected_value=True
    assert verifier_ligne(grille,colonne)==expected_value

def test_verifier_colonne_incorrecte():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,3,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    colonne=4
    expected_value=False
    assert verifier_colonne(grille,colonne)==expected_value

def test_verifier_carre_correct():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    carre=4
    expected_value=True
    assert verifier_carre(grille,carre)==expected_value

def test_verifier_carre_incorrect():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,5,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    carre=4
    expected_value=False
    assert verifier_carre(grille,carre)==expected_value

def test_verifier_grille_correcte():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    expected_value=True
    assert verifier_grille(grille)==expected_value

def test_verifier_grille_incorrecte():
    grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [1,9,5,6,5,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    expected_value=False
    assert verifier_grille(grille)==expected_value


# print(verifier_ligne([[1,3,4,5,2,8,9,6,7]],0))
# print(verifier_ligne([[1,3,4,5,2,7,9,6,7]],0))