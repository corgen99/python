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
    try:
        for i in liste:
            i=int(i)
        return True
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
    try:
        for i in liste:
            i=float(i)
        return True
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
    try:
        for i in liste:
            i=str(i)
        return True
    except:
        return False

def verification_liste_entiers(liste):
    '''
    Vérifie la sanité de la liste en entrée
    
    Entrée :
    liste (value[]) : liste de valeurs à vérifier

    Sortie :
    string : type de la liste fournie
    '''
    if verification_liste_entiers(liste):
        return "int"
    elif verification_liste_flottants(liste):
        return "float"
    else:
        print("Erreur ! La liste n'est pas composée que de nombres")

def tri_bulle(liste):
    '''
    Algorithme de tri bulle.
    Son objectif est de trier les éléments d'une liste.

    Paramètres :
    liste (float[]) : liste de valeurs à trier

    Retour :
    (float[]) : liste des mêmes valeurs triées dans l'ordre croissant
    '''

    try:
        for i in liste:
            i=float(i)
        
    except:
        print("Erreur ! La liste ne contient pas que des nombres.")


def main():
    res=0

if __name__ == "__main__":
    main()