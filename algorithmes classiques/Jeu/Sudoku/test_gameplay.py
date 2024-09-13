from creation import *
from gameplay import *
from verification import verifier_grille



grille=[[5,6,3,8,7,9,2,1,4],\
        [7,1,9,4,2,3,6,5,8],\
        [2,8,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [2,9,5,6,3,8,4,7,2],\
        [8,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]

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

def test_nombres_ligne():
    ligne=3
    expected_value=[4,2,6,1,5,7,9,8,3]
    assert nombres_ligne(grille,ligne)==expected_value

def test_nombres_colonne():
    colonne=6
    expected_value=[2,6,3,9,4,1,7,8,5]
    assert nombres_colonne(grille,colonne)==expected_value

def test_nombres_carre():
    carre=2
    expected_value=[2,1,4,6,5,8,3,9,7]
    assert nombres_carre(grille,carre)==expected_value

def test_nombres_possible():
    grille=[
        [5,6,3,8,7,9,2,1,4],\
        [0,1,9,4,2,3,6,5,0],\
        [2,0,4,5,6,1,3,9,7],\
        [4,2,6,1,5,7,9,8,3],\
        [2,9,5,6,3,8,4,7,2],\
        [0,3,7,2,9,4,1,6,5],\
        [9,4,8,3,1,5,7,2,6],\
        [6,5,1,7,4,2,8,3,9],\
        [3,7,2,9,8,6,5,4,1]]
    expected_value=[7,8]
    assert chercher_valeurs_possible(grille,1,0)==expected_value

def test_resolution():
    grille=[\
        [0,5,0,0,2,0,9,0,0],\
        [0,0,0,9,0,0,0,1,5],\
        [0,9,0,5,1,4,0,3,0],\
        [0,7,0,0,5,6,1,0,0],\
        [0,4,5,0,0,0,2,9,0],\
        [0,0,3,2,4,0,0,8,0],\
        [0,3,0,1,8,7,0,2,0],\
        [4,8,0,0,0,2,0,0,0],\
        [0,0,2,0,3,0,0,7,0],\
        ]
    
    assert verifier_grille(resoudre(grille))