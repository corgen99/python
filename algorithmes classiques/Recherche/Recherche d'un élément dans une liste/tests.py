import recherche_element

def test_aucune_correspondance():
    liste=[1,2,3,4,5,6,1,2,3,6,7,8,1,2,4,5]
    element=9
    sortie_attendue=[]
    assert recherche_element.recherche(liste,element)==sortie_attendue

def test_resultats():
    liste=[1,2,3,4,5,6,1,2,3,6,7,8,1,2,4,5]
    element=3
    sortie_attendue=[2,8]
    assert recherche_element.recherche(liste,element)==sortie_attendue