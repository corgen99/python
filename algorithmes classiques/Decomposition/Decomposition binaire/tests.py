from decomposition_binaire import decomposition_binaire_rec

def test_decomposition():
    nombre=45
    expected_output=[1,0,1,1,0,1]
    assert decomposition_binaire_rec(nombre)==expected_output
