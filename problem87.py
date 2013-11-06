# -*- encoding: utf-8 -*-
# project euler problem 87
# http://projecteuler.net/problem=87

from ProjectEulerUtils import prime_sieve

UPPER_LIMIT = 50000000

# a is the highest square root, b is the highest cube root, c is the highest 4th root
a = int(UPPER_LIMIT ** 0.5)
b = int(UPPER_LIMIT ** (1.0 / 3))
c = int(UPPER_LIMIT ** 0.25)

# all primes up to the highest square root
factors = list(prime_sieve(a))
squares = [x**2 for x in factors if x <= a]
cubes = [x**3 for x in factors if x <= b]
fourths = [x**4 for x in factors if x <= c]

# test every combination
answers = set()
for i in fourths:
    for j in cubes:
        ij = i+j
        if ij >= UPPER_LIMIT:
            break
        for k in squares:
            test = ij + k
            if test >= UPPER_LIMIT:
                break
            answers.add(test)

print len(answers)
