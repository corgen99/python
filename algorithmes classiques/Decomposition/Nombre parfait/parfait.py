import math

def decomposition_diviseurs_intuitive(nombre):
    '''
    détermine tous les diviseurs de n de manière intuitive i.e en vérifiant pour chaque nombre entre 0 et n si celui-ci divise n

    entrée :
    nombre(int) : valeur dont on veut trouver les diviseurs

    sortie :
    int[] : liste des diviseurs du nombre 
    '''
    return [i for i in range(1,nombre) if nombre%i==0]

def decomposition_diviseurs_optimisee(nombre):
    '''
    détermine tous les diviseurs de n de manière un peu plus intelligente que la manière intuitive i.e en n'effectuant que sqrt(n) opérations

    entrée :
    nombre(int) : valeur dont on veut trouver les diviseurs

    sortie :
    int[] : liste des diviseurs du nombre
    '''
    res=[1]

    borne_max=int(math.sqrt(nombre))
    for i in range(2,borne_max+1):
        if nombre%i==0:
            res.append(i)
            if nombre//i != i:
                res.append(nombre//i)
    return res

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