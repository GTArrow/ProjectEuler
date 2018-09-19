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
    count = 0
    num =2
    c=[]
    while (count<=n):
        if isPrime(num):
            count+=1
            c= c+[num]
            num+=1
        else:
            num+=1
    return c[len(c)-2]
