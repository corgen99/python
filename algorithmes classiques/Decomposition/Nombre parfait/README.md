Un nombre parfait est un nombre entier tel que la somme des ses diviseurs positif soit égale à 2n.

Par exemple, 6 est un nombre parfait car ses diviseurs entiers sont 1, 2, 3 et 6\
Et nous avons : 1+2+3+6=12 et 2*6=12

Pour l'algorithme, nous utiliserons une version simplifiée en constatant, dans notre exemple, que 6 = 1 + 2 + 3

Plus formellement, un nombre parfait n est un entier tel que σ(n) = 2n où σ(n) est la somme des diviseurs positifs de n. Ainsi 6 est un nombre parfait car ses diviseurs entiers sont 1, 2, 3 et 6, et il vérifie bien 2 × 6 = 12 = 1 + 2 + 3 + 6, ou encore 6 = 1 + 2 + 3

Entrée :\
nombre (int) : nombre à décomposer

Sortie :\
int[] : nombre binaire décomposé

La fonction décomposant le nombre n dans la base m, sa complexité est en O(log_m(n))

La terminaison de l'algorithme se justifie étant donné que l'entier décomposé est divisé au fur et à mesure par m, ce qui fait que le nombre se divise petit à petit par m

test effectué :
* Décomposition d'un nombre