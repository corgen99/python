from parfait import parfait

def test_parfait_true():
    entree=8128
    sortie_attendue=True
    assert parfait(entree)==sortie_attendue

def test_parfait_false():
    entree=87
    sortie_attendue=False
    assert parfait(entree)==sortie_attendue