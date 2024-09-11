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