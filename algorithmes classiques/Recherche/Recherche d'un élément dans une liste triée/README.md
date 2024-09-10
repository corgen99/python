Algorithme de recherche d'un élément défini dans une liste triée.

L'objectif est de trouver un élément dans une liste fournie et triée.

Entrée :
liste (value[]) : liste d'éléments triés
value (value) : valeur à rechercher

Sortie :
int[] : liste des index ressortis par la liste

Cette fonction permet de voir une manière de rechercher plus intelligemment que la recherche basique : on compare l'élément recherché à chaque valeur, et si à un moment la valeur recherchée est inférieure à la valeur dans la liste, alors on s'arrête

Cette fois-ci, la complexité n'est pas juste en O(n).
Au meilleur des cas, si la valeur est la première valeur dans le tableau ou si elle est inférieure à toutes les valeurs dans le tableau, l'algorithme est en O(1)
Au pire des cas, si la valeur est supérieure à toute valeur du tableau, on le parcourera en entier et l'algorithme sera en O(n)
En moyenne, on peut s'attendre à ce que la valeur soit environ à la moitié du tableau, soit en O(n/2)

La terminaison de l'algorithme se justifie étant donné que la liste a un nombre fini d'éléments.

test effectué :
* rechercher un élément qui n'existe pas dans la liste, résultat attendu : []
* recherche d'un élément existant