def decomposition_binaire_rec(nombre):
    '''
    Ressort la valeur binaire d'un nombre donné en entrée

    Entrée :
    nombre (int) : nombre à décomposer

    Sortie :
    int[0] : décomposition binaire du nombre
    '''
    if nombre<=1:
        return [nombre]
    
    print(nombre)
    return decomposition_binaire_rec(nombre//2)+[nombre%2]

print(decomposition_binaire_rec(6))