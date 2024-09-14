from creation import *

def test_ligne_unique():
    ligne=[[1,2,3],[1,2],[3,4,2],[1],[3]]
    expected_value=[3,4]
    assert rechercher_uniques(ligne)==expected_value

def test_compte_nombre():
    ligne=[[1,2,3],[1,2],[3,4,2],[1],[3]]
    expected_value=[3,3,3,1,0,0,0,0,0]
    assert compte_nombre(ligne)==expected_value

def test_rechercher_nombre_unique():
    ligne=[[1,2,3],[1,2],[3,4,2],[1],[3]]
    expected_value=[4]
    assert rechercher_nombre_unique(ligne)==expected_value

def test_retirer_valeurs():
    ligne=[[1,2,3],[1,2],[3,4,2],[1],[3]]
    expected_value=[[2,3],[2],[3,4,2],[1],[3]]
    assert retirer_valeurs(ligne,1)==expected_value

def test_chercher():
    ligne=[[1,2,3],[1,2],[3,4,2],[1],[3]]
    expected_value=2
    assert chercher(ligne,4)==expected_value

def test_creation_ligne():
    ligne=[[1,2,3,4,5],[1,2],[3,4,2],[1],[3],[6],[7],[8],[9]]
    expected_value=[5,2,4,1,3,6,7,8,9]
    assert creation_ligne(ligne)==expected_value

def test_creation_ligne():
    ligne=[[1,2,3,4,5],[1,2],[3,4,2],[1],[3],[6],[7],[8],[9]]
    expected_value=[5,2,4,1,3,6,7,8,9]
    assert creation_ligne(ligne)==expected_value

def test_creer_grille():
    grille=creer_grille()
    expected_value=True
    assert verifier_grille(grille)==expected_value