La suite des Syracuse est l'objet d'une conjecture bien connue en mathématiques.

La suite est définie de la manière suivante :
- Nous partons d'un entier strictement positif
- S'il est pair, on le divise par 2
- Sinon, on le multiplie par 3 et on ajoute 1

La conjecture associée suggère que la suite de Syracuse de n'importe quel entier strictement positif atteint 1.

L'objectif de la fonction qui sera créée sera de calculer la suite de Syracuse d'un nombre donné en entrée.

Entrée :
- nombre (int) : nombre dont on cherche la suite de Syracuse

Sortie :
- (int, int[]) : temps de vol de la suite et étapes atteintes avant d'atteindre 1

Complexité :
- la particularité de la suite de Syracuse est qu'on ne peut pas prédire la taille de la suite à partir d'un nombre donné, cette suite peut se résoudre aussi rapidement (ex : 16 qui atteint 1 en 5 étapes, 15 qui atteint 1 en 17 étapes et 27 qui atteint 1 en 111 étapes)

Terminaison :
- Si la conjecture de Syracuse est vraie, la terminaison de l'algorithme est justifié par cette dernière
- En l'absence de vérification de la conjecture, la terminaison n'est pas assurée _a priori_ (bien que la conjecture soit vérifiée pour tout N < 2^68)

**Améliorations possible**
- recherche de l'entier inférieur à n ayant la suite avant le plus long temps de vol