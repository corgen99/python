from min_max import min_max

def test_liste_vide():
    liste=[]
    expected_value=()
    assert min_max(liste)==expected_value

def test_liste_unaire():
    liste=[2]
    expected_value=((0,2),(0,2))
    assert min_max(liste)==expected_value

def test_liste_normale():
    liste=[2,3,4,5,1,2,6,5,1,3,4,6]
    expected_value=((4,1),(6,6))
    assert min_max(liste)==expected_value