Objectif : déterminer tous les diviseurs d'un nombre donné en entrée

Entrée :\
nombre (int) : nombre dont on cherche les diviseurs

Sortie :\
int[] : liste des diviseurs du nombre en entrée

Une version intuitive de l'algorithme consiste à parcourir tous les nombre de 1 à n et à vérifier si le nombre divise n (algorithme effectuant alors n opérations)

Une version plus optimisée de l'algorithme consiste à ne parcourir que les nombres de 1 à sqrt(n) étant donné que sqrt(n)^2 = n\
Ainsi, on exploitera de manière intelligente le fait que si un nombre i divise n, alors n/i divise n aussi\
L'algorithme permettra alors de trouver l'ensemble des diviseurs du nombre donné en entrée en \sqrt{n} opérations

La terminaison de l'algorithme se justifie étant donné que chaque nombre dispose d'un nombre fini de diviseurs

Test effectué :
* Test avec un nombre, vérifier que l'algorithme en ressort la correcte décomposition
* Test avec un nombre étant le carré d'un nombre pour vérifier que la valeur n'est pas renvoyée en double