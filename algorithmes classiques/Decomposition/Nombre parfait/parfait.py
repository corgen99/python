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

def parfait(nombre):
    '''
    détermine si un nombre est parfait

    entrée :
    nombre(int): nombre dont on veut savoir s'il est parfait ou non

    sortie:
    bool: vrai ou faux selon que le nombre soit parfait ou non
    '''
    diviseurs = decomposition_diviseurs_optimisee(nombre)
    somme_diviseurs = somme_liste(diviseurs)
    return nombre==somme_diviseurs

print(parfait(6))
print(parfait(9))
print(parfait(8128))