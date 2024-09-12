Les nombres amis sont des nombres dont la somme des diviseurs stricts de chacun des nombres est égale à l'autre nombre.

Par exemple, 220 et 284 sont amicaux car :\
Les diviseurs de 220 sont 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110\
Les diviseurs de 284 sont 1, 2, 4, 71, 142

Et nous avons :\
1+2+4+5+10+11+20+22+44+55+110=284\
1+2+4+71+142=220


Entrée :\
premier_nombre (int) : premier nombre potentiel
deuxieme_nombre (int) : deuxieme nombre à tester

Sortie :\
bool :
- vrai si les nombres sont des nombres amis
- faux sinon

L'algorithme fonctionnera de la manière suivante :
1. Dans un premier temps, l'algorithme devra trouver tous les diviseurs des deux nombres
2. Ensuite, l'algorithme calculera chaque somme de diviseurs pour déterminer si les nombres sont amis ou non

Déterminer les diviseurs de chaque nombre peut se faire en au plus \sqrt{n}+\sqrt{m} étapes (dans ce cas, pour chaque nombre on essaie de diviser le nombre avec tous les entiers compris entre 1 et sa racine carrée, ce qui nous permettra de déterminer l'ensemble des diviseurs du nombre en question)\
La vérification se fait alors en au pire \sqrt{n}+\sqrt{m} (si tous les nombres sont des diviseurs des deux nombres)

Ainsi, l'algorithme présente une complexité en O(\sqrt{n}+\sqrt{m})

La terminaison de l'algorithme se justifie étant donné que chaque nombre dispose d'un nombre fini de diviseurs

test effectué :
* Test avec deux nombres amis
* Test avec deux nombres pas amis