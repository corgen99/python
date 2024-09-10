def compare_sous_chaine(chaine,sous_chaine, i):
    '''
    Compare deux sous chaines

    Présomption : la valeur à la position i de chaine correspond au début de la sous chaine
    
    Entree :
    chaine (str) : la chaine etudiee
    sous_chaine (str) : la sous-chaine recherchée
    i : la position du début de la sous-chaine

    Sortie :
    bool : vrai si les valeurs correspondent, faux sinon
    '''
    j=1
    correspond = True
    while correspond==True and j<len(sous_chaine):
        if chaine[i+j]!=sous_chaine[j]: # si à un moment les deux valeurs sont distinctes, le résultat est faux
            correspond=False
        j+=1
            
    return correspond

def sous_chaine(chaine, sous_chaine):
    '''
    Cherche si une sous-chaine de caractères se trouve dans une chaine de caractères

    Entrée :
    chaine (str) : la chaine étudiée
    sous_chaine (str) : la chaine recherchée

    Sortie :
    int : position de la première occurrence de la chaine recherchée
    None si elle n'existe pas
    '''
    if len(chaine)==0:
        return None
    elif len(sous_chaine)==0:
        return None
    
    for i in range(len(chaine)-len(sous_chaine)+1):
        if chaine[i]==sous_chaine[0]: #cherche le début potentiel d'une sous-chaine   
            if compare_sous_chaine(chaine, sous_chaine, i):
                return i
    
    return None

chaine="Ceci est une chaine de caracteres"
sous_chaine_1=""
sous_chaine_2="est"
sous_chaine_3="caracteres"

print(sous_chaine(chaine,sous_chaine_1))
print(sous_chaine(chaine,sous_chaine_2))
print(sous_chaine(chaine,sous_chaine_3))