from graphe import *

def test_creation_noeud():
    noeud=node(0,[])
    noeud_2=node(1,noeud)
    noeud_3=node(2,noeud_2)
    expected_value=[1,[0,[]]]
    assert noeud_3.print_node()==expected_value