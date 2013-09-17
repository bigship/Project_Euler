# project euler problem 35
# http://projecteuler.net/problem=35

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

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def rotate_number(n):
    s = str(n)
    yield n
    for i in xrange(0, len(s) - 1):
        t = s[1:] + s[0]
        yield int(t)
        s = t

primes_under_one_million = prime_sieve(1000000)

cnt = 0
for prime in primes_under_one_million:
    if all(is_prime(i) for i in rotate_number(prime)):
        cnt += 1

print 'total count = %d' % cnt

