def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    primeFactor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            primeFactor = i
            n /= i
        else:
            i += 1

    if primeFactor < n:
        primeFactor = n

    return primeFactor
