# project euler problem 47
# http://projecteuler.net/problem=47

from itertools import count
from ProjectEulerUtils import is_prime

def prime_factors(n):
    s = set()
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            if is_prime(i):
                s.add(i)
            elif is_prime(n/i):
                s.add(n/i)
    return s

for value in count(647, 4):
    if len(prime_factors(value)) ==\
    len(prime_factors(value+1)) ==\
    len(prime_factors(value+2)) ==\
    len(prime_factors(value+3)) == 4:
        print value
        break

