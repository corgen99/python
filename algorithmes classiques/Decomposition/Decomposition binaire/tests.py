from decomposition_binaire import decomposition_binaire_rec, decomposition_binaire

def test_decomposition_rec():
    nombre=45
    expected_output=[1,0,1,1,0,1]
    assert decomposition_binaire_rec(nombre)==expected_output

def test_decomposition_normale():
    nombre=45
    expected_output=[1,0,1,1,0,1]
    assert decomposition_binaire(nombre)==expected_output