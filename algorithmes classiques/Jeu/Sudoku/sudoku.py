from gameplay import resoudre_intuitif
from affichage import print_belle_grille
from creation import generer_grille
from verification import verifier_grille

# grille_1=[\
#         [0,5,0,0,2,0,9,0,0],\
#         [0,0,0,9,0,0,0,1,5],\
#         [0,9,0,5,1,4,0,3,0],\
#         [0,7,0,0,5,6,1,0,0],\
#         [0,4,5,0,0,0,2,9,0],\
#         [0,0,3,2,4,0,0,8,0],\
#         [0,3,0,1,8,7,0,2,0],\
#         [4,8,0,0,0,2,0,0,0],\
#         [0,0,2,0,3,0,0,7,0],\
#         ] #entrer ici la grille à résoudre

# print("Grille initiale :")
# print_belle_grille(grille_1)

# resoudre_intuitif(grille_1)
# print()

# grille_2=[\
#         [0,0,0,0,8,0,0,0,0],\
#         [0,0,0,0,0,0,4,0,6],\
#         [9,0,7,5,0,2,0,0,0],\
#         [0,2,0,0,0,1,0,0,8],\
#         [0,0,9,8,3,0,5,0,0],\
#         [0,6,0,0,0,4,0,0,9],\
#         [1,0,8,3,0,9,0,0,0],\
#         [0,0,0,0,0,0,8,0,2],\
#         [0,0,0,0,7,0,0,0,0],\
#         ] #entrer ici la grille à résoudre

# print("Grille initiale :")
# print_belle_grille(grille_2)

# resoudre_intuitif(grille_2)
# print()

# grille_3=[\
#         [3,4,5,0,0,0,0,0,8],\
#         [6,1,0,0,8,3,5,4,9],\
#         [7,9,0,0,4,5,0,0,6],\
#         [0,0,0,1,5,7,0,0,0],\
#         [0,0,0,0,6,4,9,0,0],\
#         [0,7,1,9,0,0,4,0,0],\
#         [0,0,9,0,2,0,6,0,4],\
#         [0,5,0,0,1,0,0,0,0],\
#         [0,0,6,0,0,0,3,0,0],\
#         ] #entrer ici la grille à résoudre

# print("Grille initiale :")
# print_belle_grille(grille_3)

# resoudre_intuitif(grille_3)

# grille=creer_grille()
# print("Grille :")
# print_belle_grille(grille)
# print(f"Le sudoku est valide : {verifier_grille(grille)}")

grille=generer_grille()
print_belle_grille(grille)
grille=resoudre_intuitif(grille)
print_belle_grille(grille)