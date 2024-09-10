from recherche_sous_chaine import sous_chaine

def test_chaine_vide():
    chaine=""
    chaine_recherchee="chaine"
    expected_output=None
    assert sous_chaine(chaine, chaine_recherchee)==expected_output

def test_sous_chaine_vide():
    chaine="chaine"
    chaine_recherchee=""
    expected_output=None
    assert sous_chaine(chaine, chaine_recherchee)==expected_output

def test_chaine_absente():
    chaine="ceci est une chaine"
    chaine_recherchee="table"
    expected_output=None
    assert sous_chaine(chaine, chaine_recherchee)==expected_output

def test_chaine_dernier_mot():
    chaine="ceci est une chaine"
    chaine_recherchee="chaine"
    expected_output=13
    assert sous_chaine(chaine, chaine_recherchee)==expected_output

def test_chaine_normale():
    chaine="ceci est une chaine"
    chaine_recherchee="une"
    expected_output=9
    assert sous_chaine(chaine, chaine_recherchee)==expected_output