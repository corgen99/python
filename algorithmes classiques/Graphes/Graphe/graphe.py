class node:
    def __init__(self,numero,node_parent=None):
        self.__numero=numero
        self.__node_parent=node_parent
    
    def get_numero(self):
        return self.__numero
    
    def get_parent(self):
        return self.__node_parent
    
    def set_parent(self, node_parent):
        self.__node_parent=node_parent

    def print_node(self):
        if self.__node_parent==None:
            return None
        return [self.__node_parent.get_numero(), self.__node_parent.print_node()]
    
    def print_chemin(self):
        if self.__node_parent == None:
            print(f'{self.__numero}', sep="", end="")
        else:
            self.__node_parent.print_chemin()
            print(f' -> {self.__numero}',sep="", end="")
    
    def __str__(self):
        if self.__node_parent == None:
            return f"node[{self.__numero}, None]"
        else:
            return f"node[{self.__numero}, {self.__node_parent}]"

def trouve_enfant(liste_node, node_cherchee):
    enfants = []
    for node in liste_node:
        if node.get_parent()==node_cherchee:
            enfants.append(node)
    return enfants

# noeud=node(0)
# noeud_2=node(1,noeud)
# noeud_3=node(2,noeud_2)

# print(noeud_3)

# print(noeud.print_node())
# print(noeud_2.print_node())
# print(noeud_3.print_node())

# print(trouve_enfant())

# noeud=node(0,None)

node_0=node(0)
node_1=node(1,node_0)
node_2=node(2,node_0)
node_3=node(3,node_1)
node_4=node(4,node_1)
node_5=node(5,node_3)
node_6=node(6,node_5)
node_7=node(7,node_6)
node_8=node(8,node_3)
node_9=node(9,node_8)
node_10=node(10,node_4)

# print(node_7)
# node_7.print_chemin()

liste_node=[node_0, node_1, node_2, node_3, node_4, node_5,\
            node_6, node_7, node_8, node_9, node_10]


def afficher_node_arbre(node):
    print(f' {node.get_numero()} ', sep="", end="")

def print_enfants(liste_node, node):
    liste_enfant=trouve_enfant(liste_node, node)
    nombre_enfants=len(liste_enfant)
    taille=3*nombre_enfants
    position_parent=taille//2
    for _ in range(position_parent-1):
        print(' ', sep="", end="")

    afficher_node_arbre(node)
    print(end="\n\n")
    for nodes in liste_enfant:
        afficher_node_arbre(nodes)
    print()

# print_enfants(liste_node, node_3)

# print_enfants(liste_node, node_5)



def print_arbre(liste_node):
    '''
    crée un arbre à partir d'une liste de node
    '''
    def taille_all_blocs(liste_enfants):
        """
        retourne la taille des blocs pour chaque noeud
        """
        def taille_bloc_node(enfants, liste_enfants):
            """
            retourne la taille des blocs pour un noeud
            """
            def sum_taille(liste_node):
                """
                retourne la somme d'une liste
                """
                res=0
                for i in liste_node:
                    res += taille_bloc_node(liste_enfants[i.get_numero()], liste_enfants)
                return res

            if len(enfants)==0:
                return 3
            else:
                return sum_taille(enfants)
            
        res=[]
        for enfants in liste_enfants:
            res.append(taille_bloc_node(enfants, liste_enfants))
        return res

    def profondeur_all_nodes(liste_node):
        def profondeur_node(node):
            if node.get_parent()==None:
                return 0
            else:
                return 1+profondeur_node(node.get_parent())
        
        return [profondeur_node(nodes) for nodes in liste_node]

    def print_node(node):
        """
        affiche un noeud
        """
        for i in range(taille_blocs[node.get_numero()]//2+1):
            print(" ", end="", sep="")
        print(node.get_numero(), end="", sep="")
        for i in range(taille_blocs[node.get_numero()]//2):
            print(" ", end="", sep="")
    
    def max_liste(liste):
        res=liste[0]
        for i in liste:
            if res < i:
                res = i
        return res
    
    liste_enfants=[trouve_enfant(liste_node, nodes) for nodes in liste_node]
    
    # nombre_enfants=[len(enfants) for enfants in liste_enfants]
    taille_blocs=taille_all_blocs(liste_enfants)
    profondeur=profondeur_all_nodes(liste_node)


    # a ce stade, j'ai la liste de la profondeur de chaque node
    #   et la liste des tailles des blocs pour chaque node
    print(taille_blocs)
    print(profondeur)

    profondeur_arbre=max_liste(profondeur)
    for i in range(profondeur_arbre+1):
        for j in range(len(profondeur)):
            if profondeur[j]==i:
                print_node(liste_node[j])
        print(end="\n\n")

print_arbre(liste_node)

new_node_0=node(0,None)
new_node_1=node(1,new_node_0)
new_node_2=node(2,new_node_1)
new_node_3=node(3,new_node_2)
new_node_4=node(4,new_node_2)
new_node_5=node(5,new_node_2)
new_node_6=node(6,new_node_2)
new_node_7=node(7,new_node_1)
new_node_8=node(8,new_node_0)

liste_new_node=[new_node_0, new_node_1, new_node_2,\
                new_node_3, new_node_4, new_node_5,\
                new_node_6, new_node_7, new_node_8]

print_arbre(liste_new_node)