def wy1(a1,q,n):
    an = a1 * q ** (n-1)
    return an
def wy2(ak,q,n,k):
    an = ak * q ** (n-k)
    return an
def sum(a1,q,n):
    if(q != 1):
        suma = a1 * ((1-q**n)/(1-q))
    else:
        suma = a1*n
    return suma