# project euler problem 49
# http://projecteuler.net/problem=49

from ProjectEulerUtils import prime_sieve
from itertools import permutations, combinations

# Accroding to the problem descrption, we can eliminate 1487
four_digits_primes = [x for x in prime_sieve(10000) if len(str(x)) == 4 and x != 1487]

def prime_permutation(n):
    cnt = 0
    s = set()
    for i in permutations(str(n)):
        j = int(''.join(i))
        if j in four_digits_primes:
            s.add(j)
    return s

def solve():
    for n in four_digits_primes:
        lst = list(prime_permutation(n))
        for x, y, z in combinations(lst, 3):
            if x + z == 2*y:
                return str(x)+str(y)+str(z)

print solve()
