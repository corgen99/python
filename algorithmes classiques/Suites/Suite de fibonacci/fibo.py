def fibonacci_intuitive(nombre):
    if nombre==0:
        return 0
    elif nombre==1:
        return 1
    n_0=0
    n_1=1
    for i in range(nombre-1):
       res=n_1+n_0
       n_0=n_1
       n_1=res
    return res 

def fibonacci_rec(nombre):
    if nombre==0:
        return 0
    elif nombre==1:
        return 1
    return(fibonacci_rec(nombre-1)+fibonacci_rec(nombre-2))