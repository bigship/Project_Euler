# Project Euler utility functions

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    s = set()
    for i in xrange(1, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n/i)
    return s

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    return b

def lcm(a, b):
    return a*b / gcd(a, b)

def prime_sieve(n):
    initSieve = []
    maxNum = int(n**0.5)+1
    for i in xrange(2, n):
        initSieve.append(True)
    j = 2
    while j <= maxNum:
        if initSieve[j-2]:
            for k in xrange(j*j, n, j):
                initSieve[k-2] = False
        j += 1
    output = (x+2 for x in xrange(len(initSieve)) if initSieve[x])
    return output


