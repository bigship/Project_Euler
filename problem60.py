# project euler problem 60
# http://projecteuler.net/problem=60

# Looking for better solutions
from ProjectEulerUtils import is_prime, prime_sieve
from itertools import combinations

def is_pair(n, m):
    return is_prime(int(str(n) + str(m))) and is_prime(int(str(m) + str(n)))

def is_prime_group(it):
    for n, m in combinations(it, 2):
        if not is_pair(n, m):
            return False
    return True

primes = list(prime_sieve(10000))

def solve():
    for n in primes:
        if n == 5:
            continue
        for m in primes[primes.index(n):]:
            if is_pair(n, m):
                for x in primes[primes.index(m):]:
                    if is_prime_group([x, n, m]):
                        for y in primes[primes.index(x):]:
                            if is_prime_group([y, x, n, m]):
                                for z in primes[primes.index(y):]:
                                    if is_prime_group([z, y, x, n, m]):
                                        return sum([z, y, x, n, m])

print solve()
