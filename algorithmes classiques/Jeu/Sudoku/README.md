L'objectif ici est de faire un programme pour résoudre une grille de sudoku

La grille sera représentée par une liste de liste de liste, par exemple :\
[   [5,6,3,8,7,9,2,1,4],\
    [7,1,9,4,2,3,6,5,8],\
    [2,8,4,5,6,1,3,9,7],\
    [4,2,6,1,5,7,9,8,3],\
    [1,9,5,6,3,8,4,7,2],\
    [8,3,7,2,9,4,1,6,5],\
    [9,4,8,3,1,5,7,2,6],\
    [6,5,1,7,4,2,8,3,9],\
    [3,7,2,9,8,6,5,4,1]]

Dans un premier temps, une fonction permettant de créer une nouvelle grille de sudoku sera réalisée.

Ensuite, une fonction permettant de vérifier si une grille est correcte ou non sera créée

Des fonctions annexes (placer numéro, chercher les valeurs probables) seront ensuite réalisées

Enfin le programme pour résoudre la grille sera réalisé.

En l'état actuel, la résolution est faite d'une manière très intuitive, sans beaucoup de logique derrière (regarder les valeurs possibles dans chaque case, s'il y a une case n'ayant qu'une valeur possible, y mettre la valeur)


**Améliorations envisageable :**
- faire une résolution plus intelligente (par exemple : si 2 cases alignées ne peuvent contenir que 2 valeurs, alors les autres cases de la ligne ne pourront pas contenir ces valeurs)
- faire en sorte qu'il soit plus simple de mettre une grille en entrée
- ajouter un module pour générer automatiquement une grille
- ajouter une interface graphique pour que l'ensemble soit plus lisible
