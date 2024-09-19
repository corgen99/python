from insertion import tri_insertion

def test_tri():
    liste=[0,2,3,2,1,1,8,4,6,7,9,1,2]
    expected_value=[0,1,1,1,2,2,2,3,4,6,7,8,9]
    assert tri_insertion(liste) == expected_value