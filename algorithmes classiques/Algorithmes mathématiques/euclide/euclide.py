def PGCD(a,b):
    def echanger(a,b):
        return b,a    

    res=1
    while a>0 and b>0:
        if a<b:
            a,b=echanger(a,b)
        a=a%b
    return max(a,b)

def PGCD_rec(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    return PGCD(a%b,b)    