def eratosthene(nombre):
    res=[i for i in range(2,nombre)]
    
    for valeur in res:
        for j in range(2,nombre//valeur+1):
            if valeur*j in res:
                res.remove(valeur*j)
    return res

print(eratosthene(100))
print(eratosthene(1000))