def echange(liste, indice):
    tmp=liste[indice]
    liste[indice]=liste[indice-1]
    liste[indice-1]=tmp
    return liste

def ranger(liste, indice):
    for i in range(indice,1, -1):
        if liste[i]<liste[i-1]:
            liste=echange(liste, i)
        else:
            break
    return liste

def tri_insertion(liste):
    for i in range(2,len(liste)):
        liste=ranger(liste,i)
    return liste