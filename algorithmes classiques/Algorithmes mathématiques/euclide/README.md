L'algorithme d'euclide a pour objectif de calculer le PGCD de deux nombres

Il fonctionne sur le constat que, pour deux nombres a,b :

PGCD(a,b)=PGCD(b,a-b)

Ainsi :
PGCD(251,123) = PGCD(251-123,123)\
= PGCD(128,123) = PGCD(128-123,123)\
= PGCD(123,5) = ... = PGCD(3,5) = 1

Pour aller un peu plus vite, il est possible de passer par la division euclidienne et de ne garder que son reste, ainsi :

PGCD(a,b)=PGCD(a%b,b)