def f(n):
    if n<=1:
        return n
    else:
        return(f(n-1)+f(n-2))

t = 30
sum = 0
for i in range(2,35):
    if f(i)<=4000000 and f(i)%2==0:
        print (f(i))
        sum = sum + f(i)

print (sum)

        
