def decomposition_binaire_rec(nombre):
    '''
    Ressort la valeur binaire d'un nombre donné en entrée (de manière récursive)

    Entrée :
    nombre (int) : nombre à décomposer

    Sortie :
    int[] : décomposition binaire du nombre
    '''
    if nombre<=1:
        return [nombre]
    
    return decomposition_binaire_rec(nombre//2)+[nombre%2]

print(decomposition_binaire_rec(6))

def decomposition_binaire(nombre):
    '''
    Ressort la valeur binaire d'un nombre donné en entrée

    Entrée :
    nombre (int) : nombre à décomposer

    Sortie :
    int[] : décomposition binaire du nombre
    '''
    res=[]
    while nombre>1:
        res=[nombre%2]+res
        nombre=nombre//2
    res=[nombre]+res
    return res

print(decomposition_binaire(6))