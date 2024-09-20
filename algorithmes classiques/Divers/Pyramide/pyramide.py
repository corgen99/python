def pyramide(hauteur):
    for i in range(hauteur):
        nombre_espaces = hauteur-i
        for j in range(nombre_espaces):
            print(" ",end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

pyramide(8)