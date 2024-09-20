class node:
    def __init__(self,numero,node_parent=""):
        self.__numero=numero
        self.__node_parent=node_parent
    
    def get_numero(self):
        return self.__numero
    
    def get_parent(self):
        return self.__node_parent
    
    def set_parent(self, node_parent):
        self.__node_parent=node_parent

    def print_node(self):
        if self.__node_parent==[]:
            return []
        return [self.__node_parent.get_numero(), self.__node_parent.print_node()]
    
    def __str__(self):
        if self.__node_parent == []:
            print(f"node[{self.__numero},[]]")
        else:
            print(f"node[{self.__numero},",end="")
            print(self.__node_parent, end="")
            print("]",end="")

def trouve_enfant(liste_node, node_cherchee):
    enfants = []
    for node in liste_node:
        if node.node_parent==node_cherchee:
            enfants.append(node)
    return enfants

noeud=node(0,[])
noeud_2=node(1,noeud)
noeud_3=node(2,noeud_2)

print(noeud_3)

# print(noeud.print_node())
# print(noeud_2.print_node())
# print(noeud_3.print_node())

# print(trouve_enfant())