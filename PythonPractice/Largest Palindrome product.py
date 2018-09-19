def Ispalindrome(n):
    c = False
    for i in range(int(len(str(n))/2)):
        if str(n)[i]==str(n)[len(str(n))-1-i] and i<len(str(n))-1-i:
            c = True
        else:
            c = False
            break
    return c

def l():
    largest = 0
    for i in range(100,1000):
        for j in range(i,1000):
            if Ispalindrome(i*j) and i*j > largest:
                largest = i*j
    print (largest)
