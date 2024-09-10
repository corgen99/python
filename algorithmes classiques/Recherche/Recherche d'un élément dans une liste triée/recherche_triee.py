def recherche_triee(liste, valeur):
    '''
    Recherche un élément dans une liste triee fournie
    On suppose que la liste est triée

    Entree :
    liste : liste de valeurs triee
    valeur : valeur à rechercher dans la liste

    Retour :
    liste des positions de la valeur recherchée dans la liste
    [] si la valeur n'est pas trouvée dans la liste
    '''
    res=[]
    i=0
    while i < len(liste) and liste[i] <= valeur: 
        if liste[i] == valeur:
            res.append(i)
        i+=1
    return res

liste=[1,1,1,2,2,3,4,5,5,5,5,6,6,7,8,8]
element=5
print(recherche_triee(liste, element))