Recherche d'une sous-chaine dans une chaine de caractère

L'objectif de l'algorithme est de trouver si une sous-chaine se situe dans une chaîne de caractères.

Entrée :\
chaine (str) : chaine de caractère\
sous_chaine (str) : sous chaine recherchée

Sortie :\
int : position de la première occurrence de la sous-chaine
 
La fonction parcourant la chaîne de caractère une fois, sa complexité est en O(n) avec n la longueur de la chaine de caractère

La terminaison de l'algorithme se justifie étant donné que la chaîne de caractère a un nombre fini d'éléments

Tests effectués :
* lancer l'algorithme sur une chaîne de caractère vide, résultat attendu : -1
* lancer l'algorithme sur une sous-chaîne vide, résultat attendu : -1
* lancer l'algorithme avec une sous-chaine n'étant pas dans la chaîne de caractère, résultat attendu : -1
* lancer l'algorithme avec une sous-chaine qui match juste au dernier mot
* lancer l'algorithme sur une liste classique et une chaîne de caractères classiques