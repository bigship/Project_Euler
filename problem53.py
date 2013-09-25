# project euler problem 53
# http://projecteuler.net/problem=53

from math import factorial

cnt = 0
for n in xrange(100, 0, -1):
    for r in xrange(1, n):
        if factorial(n) / (factorial(r)*factorial(n-r)) >= 1000000:
            cnt += 1

print cnt