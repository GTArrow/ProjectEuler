def dev(n):
    count = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            count += 1
    return count+1
    
def a(n):
    count = 0
    i = 110
    while True:
        if dev(i)==n:
            return i % 500500507
        else:
            i+=1
