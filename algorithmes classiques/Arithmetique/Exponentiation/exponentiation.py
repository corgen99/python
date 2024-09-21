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

def exponentiation_intuitive(nombre, exposant):
    """
    version intuitive de l'exponentiation
    complexité en O(e) avec E l'exposant recherché
    """
    res=1
    for i in range(exposant):
        res*=nombre
    return res

def exponentiation_optimisee(nombre, exposant):
    """
    version optimisee de l'exponentiation utilisant de manière intelligente la décomposition binaire de l'exposant
    complexité en O(log2(e) avec e l'exposant souhaité)
    """
    decomp = decomposition_binaire_rec(exposant)
    print(decomp)
    res=1
    for i in range(len(decomp)-1,-1, -1):
        if decomp[i]==1:
            res*=nombre
        nombre*=nombre
    return res

# print(exponentiation_optimisee(2,6))

def exponentiation_recursive(nombre,exposant):
    """
    version recursive de l'exponentiation
    le résultat se fait en E étapes avec E la valeur de l'exposant
    """
    if exposant==0:
        return 1
    return nombre*exponentiation_recursive(nombre, exposant-1)

# print(exponentiation_recursive(2,6))