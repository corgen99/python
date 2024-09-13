from affichage import *
from verification import verifier_grille
from gameplay import resoudre

grille=[\
[0,5,0,0,2,0,9,0,0],\
[0,0,0,9,0,0,0,1,5],\
[0,9,0,1,5,4,0,3,0],\
[0,7,0,0,5,6,1,0,0],\
[0,4,5,0,0,0,2,9,0],\
[0,0,3,2,4,0,0,8,0],\
[0,3,0,1,8,7,0,2,0],\
[4,8,0,0,0,2,0,0,0],\
[0,0,2,0,3,0,0,7,0],\
]

print_belle_grille(resoudre(grille))