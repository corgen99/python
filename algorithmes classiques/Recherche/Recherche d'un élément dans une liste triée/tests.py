import recherche_triee

def test_aucune_correspondance():
    liste=[1,1,1,2,2,3,4,5,5,5,5,6,6,7,8,8]
    element=9
    sortie_attendue=[]
    assert recherche_triee.recherche_triee(liste,element)==sortie_attendue

def test_resultats():
    liste=[1,1,1,2,2,3,4,5,5,5,5,6,6,7,8,8]
    element=5
    sortie_attendue=[7,8,9,10]
    assert recherche_triee.recherche_triee(liste,element)==sortie_attendue