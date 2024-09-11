from diviseurs import *

def test_decomposition_intuitive():
    nombre_a_decomposer=632
    decomposition_attendue=[1,2,4,8,79,158,316]
    assert decomposition_diviseurs_intuitive(nombre_a_decomposer)==decomposition_attendue

def test_decomposition_optimisee():
    nombre_a_decomposer=632
    decomposition_attendue=[1,2,316,4,158,8,79]
    assert decomposition_diviseurs_optimisee(nombre_a_decomposer)==decomposition_attendue

def test_decomposition_intuitive_carre():
    nombre_a_decomposer=49
    decomposition_attendue=[1,7]
    assert decomposition_diviseurs_intuitive(nombre_a_decomposer)==decomposition_attendue

def test_decomposition_optimisee_carre():
    nombre_a_decomposer=49
    decomposition_attendue=[1,7]
    assert decomposition_diviseurs_optimisee(nombre_a_decomposer)==decomposition_attendue