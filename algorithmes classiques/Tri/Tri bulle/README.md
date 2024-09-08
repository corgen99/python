Le tri bulle est un algorithme de tri classique, un des exemples les plus commun pour faire aborder la notion de tri aux étudiants.

Cet algorithme, assez naturel, fonctionne de la manière suivante:\
- On part de la première valeur de la liste à trier
- A chaque itération, on compare la valeur sélectionnée par rapport à la valeur à sa droite
    - Si la valeur sélectionnée est plus grande, on échange les deux valeurs
    - Sinon, on sélectionne la valeur à sa droite

A chaque itération, l'algorithme fait alors remonter les valeurs extrêmes comme des bulles de savon monteraient dans l'air.

Bien qu'intuitif, ce tri n'est pas le plus efficace.\
En effet, à chaque itération on parcourt l'entièreté de la liste, et nous devons itérer autant de fois qu'il y a de valeurs dans la liste.\
L'algorithme possède donc une complexité en O(n^2), tandis que les meilleurs algorithmes de tri possèdent des complexités en O(n log(n)) (complexités atteintes avec des algorithmes fonctionnant selon le principe de "diviser pour régner")

L'algorithme dispose au mieux d'une complexité en O(n) si toute la liste est triée

La terminaison de l'algorithme se justifie en constatant qu'à chaque itération, au moins une nouvelle valeur est bien triée.\
Ainsi, la suite de l'ensemble des valeurs "non-triées" à chaque itération est une suite strictement décroissante et bornée.\
Elle atteint donc sa borne.