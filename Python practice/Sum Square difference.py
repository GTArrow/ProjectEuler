def f(n):
    sum = 0
    square = 0
    for i in range(1,n+1):
        sum+=i
    sum =sum**2
    for i in range(1,n+1):
        square += i**2
    dif = sum- square
    return dif

    
