from decomposition_base import decomposition_base_rec, decomposition_base

def test_decomposition_rec():
    nombre=90
    base=25
    expected_output=[3,15]
    assert decomposition_base_rec(nombre,base)==expected_output

def test_decomposition():
    nombre=90
    base=25
    expected_output=[3,15]
    assert decomposition_base(nombre,base)==expected_output