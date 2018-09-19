def f(n):
    prod = 0
    c=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            prod = i**2+j**2
            c = n-i-j
            if prod == c**2 and 0<c<int(n/2)+1:
                return i*j*c
        
