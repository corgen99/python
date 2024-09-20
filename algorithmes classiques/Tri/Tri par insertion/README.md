Le tri par insertion est une méthode de tri simple et intuitive qui s'inspire de la façon dont nous trions naturellement des objets dans la vie quotidienne, comme des cartes à jouer.

L'idée fondamentale est de construire progressivement un tableau trié en prenant un élément à la fois du tableau non trié et en l'insérant à la bonne position dans la partie déjà triée.

Le processus commence avec un seul élément considéré comme trié, puis chaque nouvel élément est comparé aux éléments déjà triés et placé à l'endroit approprié. Cette opération est répétée jusqu'à ce que tous les éléments aient été insérés dans la partie triée.

Ce tri est particulièrement efficace pour les petits ensembles de données ou pour des ensembles qui sont déjà partiellement triés. Il est stable, ce qui signifie qu'il préserve l'ordre relatif des éléments égaux.

Bien que simple à comprendre et à mettre en œuvre, le tri par insertion n'est généralement pas le plus efficace pour de grands ensembles de données non triées, car sa complexité temporelle dans le pire des cas est quadratique.

Complexité temporelle :
- Dans le meilleur cas, c'est en O(n) (si tous les éléments sont triés dans l'ordre croissant, on parcourt une fois la liste)
- Dans le pire cas, on est en O(n^2) (si la liste est triée en ordre décroissant, à chaque étape on parcourt l'entièreté de la partie déjà triée, ce qui donne 
    - 1+2+...+n-2+n-1 = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = {n^2-n}{2}
- étapes)
- En moyenne, on peut considérer qu'on ne parcourt que la moitié de la liste déjà triée, ce qui donne une complexité en moyenne en O(n^2) (\frac{n^2-n}/4)