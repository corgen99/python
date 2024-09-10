Algorithme de recherche de la valeur minimale et maximale d'une liste.

Présomption : la liste contient des valeurs homogènes et comparables.

Entrée :\
liste (value[]) : liste de valeurs comparables

Sortie :\
((int,valeur), (int,valeur)) : couple des couples (position, valeur) des valeurs minimale et maximale de la liste\
    La position retournée est la première occurence de la valeur minimale et maximale
 
La fonction parcourant la liste une fois, sa complexité est en O(n)

La terminaison de l'algorithme se justifie étant donné que la liste a un nombre fini d'éléments.

Tests effectués :
* lancer l'algorithme sur une liste vide, valeur attendue : (0,0)
* lancer l'algorithme sur une liste contenant une seule valeur
* lancer l'algorithme sur une liste classique