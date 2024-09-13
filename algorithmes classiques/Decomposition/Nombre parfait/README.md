Un nombre parfait est un nombre entier tel que la somme des ses diviseurs positif soit égale à 2n.

Par exemple, 6 est un nombre parfait car ses diviseurs entiers sont 1, 2, 3 et 6\
Et nous avons : 1+2+3+6=12 et 2*6=12

Pour l'algorithme, nous utiliserons une version simplifiée en constatant, dans notre exemple, que 6 = 1 + 2 + 3

Plus formellement, un nombre parfait n est un entier tel que σ(n) = 2n où σ(n) est la somme des diviseurs positifs de n. Ainsi 6 est un nombre parfait car ses diviseurs entiers sont 1, 2, 3 et 6, et il vérifie bien 2 × 6 = 12 = 1 + 2 + 3 + 6, ou encore 6 = 1 + 2 + 3

Entrée :\
nombre (int) : nombre à tester

Sortie :\
bool :
- vrai si le nombre est un nombre parfait
- faux sinon

L'algorithme fonctionnera de la manière suivante :
1. Dans un premier temps, l'algorithme devra trouver tous les diviseurs de n
2. Ensuite, l'algorithme calculera la somme des diviseurs de n pour déterminer si le nombre est parfait ou non

Pour trouver l'ensemble des diviseurs de n, il s'agira de décomposer le nombre en facteurs premiers puis de calculer l'ensemble des diviseurs existants

Déterminer les diviseurs peut se faire en au plus \sqrt{n} étapes (dans ce cas, on essaie de diviser n avec tous les entiers compris entre 1 et \sqrt{n}, ce qui nous permettra de déterminer l'ensemble des diviseurs de n)\
La vérification se fait alors en au pire \sqrt{n} (si tous les nombres sont des diviseurs de n)

Ainsi, l'algorithme présente une complexité en O(\sqrt{n})

La terminaison de l'algorithme se justifie étant donné que chaque nombre dispose d'un nombre fini de diviseurs

test effectué :
* Test avec un nombre parfait
* Test avec un nombre pas parfait

**Améliorations possibles**
- calculer les nombres parfaits inférieurs à une valeur donnée