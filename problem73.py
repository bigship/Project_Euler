# -*- encoding: utf-8 -*-
# project euler problem 73
# http://projecteuler.net/problem=73

import time

def gcd(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    else:
        return gcd(a, b%a)

start = time.time()
count = 0
for b in xrange(2, 12001):
    for a in xrange(int(b/3) + 1, int(b/2) + 1):
        if gcd(a, b) == 1:
            if 3*a > b and 2*a < b:
                count += 1

print count
end = time.time() - start
print 'It took %f seconds.' % end