# -*- encoding: utf-8 -*-
# project euler problem 108
# http://projecteuler.net/problem=108

import time, itertools

start = time.time()
prime = [2, 3, 5, 7, 11, 13, 17]

def primeFactors(n):
    d = {}
    length = len(prime)
    i = 0
    while i < length:
        if n % prime[i] == 0:
            if prime[i] not in d:
                d[prime[i]] = 1
            else:
                d[prime[i]] += 1
            n /= prime[i]
            if n == 1:
                return d
        else:
            i += 1

def divisorsOfSquare(n):
    count = 1
    d = primeFactors(n)
    if d == None:
        return None
    for v in d.values():
        count *= (2*v+1) 
    return count

for i in itertools.count(2):
    t = divisorsOfSquare(i)
    if t != None:
        if (t + 1) / 2 > 1000:
            print i
            break

end = time.time() - start
print 'It took %f seconds' % end