La fonction factorielle est un exemple classique d'algorithme récursif.\\
Lorsqu'on travaille dans l'ensemble des entiers naturels, la factorielle est définie comme suit : f(n)=n*(n-1)*(n-2)*...*2*1\\
Dit autrement, la factorielle de n, écrite autrement n!, correspond au produit des entiers de 1 à n

Cette fonction est un exemple classique d'algorithme récursif, puisqu'il vient alors que :
f(1)=1
f(n)=n*(n-1)*(n-2)*...*2*1

Or, f(n-1)=(n-1)*(n-2)*...*2*1

Ainsi, f(n)=n*f(n-1)

La structure récursive de la fonction apparait.

On peut aussi calculer f(0) en utilisant la définition précédente :
f(1)=1*f(0)

Or f(1)=1, donc f(0)=1

Terminaison :
    Nous travaillons dans l'ensemble des entiers naturels, ensemble dont la borne minimale est 0
    A chaque nouvel appel, la valeur appelée décrémente
    Ainsi, les valeurs appelées constituent une suite strictement décroissante avec une borne minimale, donc elle atteint sa borne et l'algorithme se termine

Complexité en temps :
    O(n) avec n la valeur d'appel => la fonction factorielle est appelée n+1 fois afin de trouver le résultat

Liste des tests réalisés :
-> test des erreurs possibles (nombre négatif, nombre à virgule, caractère n'étant pas un nombre, booléen)
-> test du résultat