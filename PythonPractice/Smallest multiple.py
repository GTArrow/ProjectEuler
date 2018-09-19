def check(b,n):
    a=True
    for i in range(1,n+1):
        if b%i==0:
            a=True
        else:
            a=False
            break
    return a


def f():
    b = 2520
    while(True):
        if check(b,20):
            break
        else:
            b=b+1
    return b
        
