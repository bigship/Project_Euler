# -*- encoding: utf-8 -*-
# project euler problem 70
# http://projecteuler.net/problem=70

# A prime number must end in 1, 3, 7, 9 and φ(n) = n-1 would only change the last digit.
# So they cannot be permutations of each other, which means what we're looking for is not
# a prime number. (even though the prime number closest to 1e7 can make n/φ(n) minimal)
# The next best choice would be a number which has two distinct prime factors where each is 
# close to sqrt(1e7) (because φ(m*n) = φ(m)*φ(n), where m and n are relatively prime).

from itertools import combinations
from math import sqrt
from ProjectEulerUtils import prime_sieve

pairs = combinations(prime_sieve(2*int(sqrt(1e7))), 2)
minimal = (100, 0)
for n, t in ((a*b, (a-1)*(b-1)) for a, b in pairs if a*b < 1e7):
    ratio = float(n) / t
    if ratio < minimal[0] and sorted(str(n)) == sorted(str(t)):
        minimal = (ratio, n)
print minimal