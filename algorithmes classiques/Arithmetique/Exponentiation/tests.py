from exponentiation import exponentiation_intuitive, exponentiation_optimisee, exponentiation_recursive

def test_exponentiation_intuitive():
    nombre=5
    exposant=4
    expected_value=pow(5,4)
    assert exponentiation_intuitive(nombre, exposant)==expected_value

def test_exponentiation_optimisee():
    nombre=5
    exposant=4
    expected_value=pow(5,4)
    assert exponentiation_optimisee(nombre, exposant)==expected_value

def test_exponentiation_recursive():
    nombre=5
    exposant=4
    expected_value=pow(5,4)
    assert exponentiation_recursive(nombre, exposant)==expected_value