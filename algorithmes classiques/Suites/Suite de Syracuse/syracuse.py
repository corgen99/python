def syracuse_intuitive(nombre):
    '''
    Calcule la suite de Syracuse d'un nombre de manière intuitive

    Paramètres :
    - nombre (int) : nombre dont on cherche la suite de Syracuse

    Sortie :
    - (int, int[]) : temps de vol de la suite et liste des nombres atteints par la suite issue du nombre entré en paramètre
    '''
    res=[]
    temps_de_vol=0
    while nombre !=1:
        res.append(nombre)
        temps_de_vol+=1
        if nombre%2==0:
            nombre=nombre//2
        else:
            res.append(nombre*3+1)
            nombre=(nombre*3+1)//2
            temps_de_vol+=1
    
    temps_de_vol+=1
    res.append(nombre)
    return temps_de_vol, res

def syracuse_rec(nombre):
    '''
    Calcule la suite de Syracuse d'un nombre de manière récursive

    Paramètres :
    - nombre (int) : nombre dont on cherche la suite de Syracuse

    Sortie :
    - (int, int[]) : temps de vol de la suite et liste des nombres atteints par la suite issue du nombre entré en paramètre
    '''
    if nombre==1:
        return 1,[1]
    elif nombre%2==0: # le nombre est pair
        res=syracuse_rec(nombre//2)
        return res[0]+1, [nombre]+res[1]
    else:
        res=syracuse_rec((nombre*3+1)//2)
        return res[0]+2, [nombre, nombre*3+1]+res[1]

print(syracuse_intuitive(11))
print(syracuse_rec(11))