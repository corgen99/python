import euclide

def test_pgcd():
    a=251
    b=123
    expected_value=1
    assert euclide.PGCD(a,b)==expected_value

def test_pgcd_2():
    a=21
    b=15
    expected_value=3
    assert euclide.PGCD(a,b)==expected_value

def test_pgcd_rec():
    a=251
    b=123
    expected_value=1
    assert euclide.PGCD(a,b)==expected_value

def test_pgcd_rec_2():
    a=21
    b=15
    expected_value=3
    assert euclide.PGCD(a,b)==expected_value