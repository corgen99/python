from decomposition_diviseurs import decomposition_diviseurs_optimisee

def somme_liste(liste):
    '''
    calcule la somme des éléments d'une liste

    entrée :
    liste(int[]) : liste dont on veut la somme des nombres

    sortie :
    int : somme des nombres de la liste
    '''
    res=0
    for i in liste:
        res+=i
    return res

def amis(a,b):
    '''
    détermine si deux nombres sont amis

    entrée :
    a,b(int): nombres dont on veut savoir s'il est sont amis ou non

    sortie:
    bool: vrai ou faux selon que les nombres sont amis ou non
    '''
    diviseurs_a = decomposition_diviseurs_optimisee(a)
    diviseurs_b = decomposition_diviseurs_optimisee(b)
    somme_diviseurs_a = somme_liste(diviseurs_a)
    somme_diviseurs_b = somme_liste(diviseurs_b)
    return somme_diviseurs_a==b and somme_diviseurs_b==a

print(amis(220,284))
print(amis(330,362))
print(amis(6232,6368))