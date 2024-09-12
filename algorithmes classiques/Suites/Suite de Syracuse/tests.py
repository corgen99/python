from syracuse import *

def test_syracuse_intuitive():
    nombre = 15
    resultat_attendu = (18, [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    assert syracuse_intuitive(nombre)==resultat_attendu

def test_syracuse_recursive():
    nombre = 15
    resultat_attendu = (18, [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    assert syracuse_rec(nombre)==resultat_attendu