import fibo

def test_fibonacci_intuitive_0():
    nombre=0
    expected_value=0
    assert fibo.fibonacci_intuitive(nombre)==expected_value

def test_fibonacci_intuitive_1():
    nombre=1
    expected_value=1
    assert fibo.fibonacci_intuitive(nombre)==expected_value

def test_fibonacci_intuitive_5():
    nombre=5
    expected_value=5
    assert fibo.fibonacci_intuitive(nombre)==expected_value

def test_fibonacci_rec_0():
    nombre=0
    expected_value=0
    assert fibo.fibonacci_rec(nombre)==expected_value

def test_fibonacci_rec_1():
    nombre=1
    expected_value=1
    assert fibo.fibonacci_rec(nombre)==expected_value

def test_fibonacci_rec_5():
    nombre=5
    expected_value=5
    assert fibo.fibonacci_rec(nombre)==expected_value