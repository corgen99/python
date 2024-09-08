import verifications
import time

def permuter_voisins(liste, index):
    '''
    Permuter la valeur dans une liste avec sa case adjacente
    '''
    temp=liste[index]
    liste[index]=liste[index+1]
    liste[index+1]=temp
    return liste

def tri_bulle_etape(liste):
    '''
    Joue une étape du tri bulle
    -> parcourir la liste de gauche à droite
    -> si la valeur à l'index étudié est supérieurs à la valeur à sa droite, permuter
    -> sinon, ne rien faire
    '''
    for i in range(len(liste)-1):
        if (liste[i] > liste[i+1]): # si la valeur à gauche est supérieure à la valeur de droite, on intervertit les deux valeurs
            permuter_voisins(liste, i)
    return liste

def tri_bulle(liste):
    '''
    Algorithme de tri bulle.
    Son objectif est de trier les éléments d'une liste.

    Paramètres :
    liste (float[]) : liste de valeurs à trier

    Retour :
    (float[]) : liste des mêmes valeurs triées dans l'ordre croissant
    '''
    if verifications.verification_liste(liste):
        for i in range(len(liste)):
            liste = tri_bulle_etape(liste)
        return liste
    else :
        print("Erreur ! La liste fournie n'est pas homogène")
        return liste
    

def main():
    liste=input("Entrez la liste que vous souhaitez trier : ")
    liste=liste.split()
    start_time = time.time()
    liste_triee=tri_bulle(liste)
    stop_time = time.time()
    print(f"La liste triée est : {liste_triee}")
    print(f"La liste a été triée en {stop_time-start_time} secondes")

if __name__ == "__main__":
    main()