from creation import *
from gameplay import *

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