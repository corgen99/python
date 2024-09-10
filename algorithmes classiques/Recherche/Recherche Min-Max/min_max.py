def min_max(liste):
    if liste==[]:
        return ()
    
    min=liste[0]
    pos_min=0
    max=liste[0]
    pos_max=0

    for i in range(len(liste)):
        if liste[i] < min:
            min=liste[i]
            pos_min=i
        if liste[i] > max:
            max=liste[i]
            pos_max=i
        
    return (pos_min,min), (pos_max,max)

liste=[5,6,1,5,4,3,1,4,5,6,2]
print(min_max(liste))