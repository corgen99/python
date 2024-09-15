import eratosthene

def test_eratosthene():
    nombre=20
    expected_value=[2,3,5,7,11,13,17,19]
    assert eratosthene.eratosthene(nombre)==expected_value