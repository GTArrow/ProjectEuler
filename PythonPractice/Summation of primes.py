def isPrime(n):
    a= True
    for i in range(2,int(n/2)+1):
        if n%i==0:
            a=False
            break
        else:
            a = True
    return a

def f(n):
    sum = 0
    for i in range(2,n):
        if isPrime(i):
            sum+=i
    return sum
