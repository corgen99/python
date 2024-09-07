def factorielle_recursive(n):
    '''
    Calcule la factorielle de n de manière récursive.

    Parametres:
    n (int) : le nombre dont on désire la factorielle

    Renvoie:
    int: la factorielle de n
    '''
    if n==0:
        return 1
    elif n > 0 :
        return n*factorielle_recursive(n-1)
    else:
        print("Erreur ! Le nombre doit être un entier positif.")

def main():
    try:
        n = int(input("Entrez le nombre dont vous souhaitez la factorielle : "))
        if(n < 0):
            print("Erreur ! Le nombre doit être un entier positif.")
        else:
            print(f"{n}! = {factorielle_recursive(n)}")

    except:
        print("Erreur ! La valeur fournie n'est pas un nombre entier, essayez encore...")

if __name__ == "__main__":
    main()