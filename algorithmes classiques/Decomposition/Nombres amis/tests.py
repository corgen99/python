from amis import amis

def test_amis_true():
    entree_a=6232
    entree_b=6368
    sortie_attendue=True
    assert amis(entree_a, entree_b)==sortie_attendue

def test_amis_false():
    entree_a=6232
    entree_b=6364
    sortie_attendue=False
    assert amis(entree_a, entree_b)==sortie_attendue