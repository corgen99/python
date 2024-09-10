Algorithme de recherche d'un élément défini dans une liste.

L'objectif est de trouver un élément dans une liste fournie.

Entrée :\
liste (value[]) : liste d'éléments\
value (value) : valeur à rechercher

Sortie :\
int[] : liste des index ressortis par la liste

Cette fonction permet de présenter le fonctionnement des listes de manière simple et intuitive : elle va parcourir la liste, comparer chaque valeur de la liste à la valeur souhaitée, et enregistrer dans la liste de sortie les index trouvés

La fonction parcourant la liste une fois, sa complexité est en O(n)

La terminaison de l'algorithme se justifie étant donné que la liste a un nombre fini d'éléments.

test effectué :
* rechercher un élément qui n'existe pas dans la liste, résultat attendu : []
* recherche d'un élément existant