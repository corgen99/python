def decomposition_base_rec(nombre,base):
    '''
    Ressort la décomposition d'un nombre donné dans la base voulue

    Entrée :
    nombre (int) : nombre à décomposer
    base (int) : base de la décomposition

    Sortie :
    int[] : décomposition binaire du nombre
    '''
    if nombre<=base:
        return [nombre]
    
    return decomposition_base_rec(nombre//base, base)+[nombre%base]

print(decomposition_base_rec(23,8))