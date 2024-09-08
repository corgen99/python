def verification_liste_entiers(liste):
    '''
    Vérifie la sanité de la liste en entrée
    
    Entrée :
    liste (int[]) : liste de valeurs à vérifier

    Sortie :
    bool : 
    - True si la liste n'est composée que d'entiers
    - False sinon
    '''
    res=True
    try:
        for i in liste:
            if i!=int(i):
                res=False
        return res
    except:
        return False

def verification_liste_flottants(liste):
    '''
    Vérifie la sanité de la liste en entrée
    
    Entrée :
    liste (float[]) : liste de valeurs à vérifier

    Sortie :
    bool : 
    - True si la liste n'est composée que de nombres
    - False sinon
    '''
    res=True
    try:
        for i in liste:
            if i!=float(i):
                res=False
        return res
    except:
        return False

def verification_liste_str(liste):
    '''
    Vérifie la sanité de la liste en entrée
    
    Entrée :
    liste (str[]) : liste de valeurs à vérifier

    Sortie :
    bool : 
    - True si la liste n'est composée que de chaînes de caractères
    - False sinon
    '''
    res=True
    try:
        for i in liste:
            if i!=str(i):
                res=False
        return res
    except:
        return False

def verification_liste(liste):
    '''
    Vérifie la sanité de la liste en entrée
    
    Entrée :
    liste (value[]) : liste de valeurs à vérifier

    Sortie :
    bool :
    - True si la liste est uniforme en type de données
    - False sinon
    '''
    if verification_liste_entiers(liste) or verification_liste_flottants(liste) or verification_liste_str(liste):
        return True
    else:
        return False