# project euler problem 41
# http://projecteuler.net/problem=41

# sum(xrange(1, 9))  = 36, divisible by 3
# sum(xrange(1, 10)) = 45, divisible by 3
# So any 8-digit or 9-digit numbers are not what we want.
# The problem asks for the largest n-digit pandigital prime number,
# we can make use of the permutations, in this way we don't even need
# to compute any prime numbers in advance.
# Tricky part: we really should let itertools.permutations provide all the permutations in 
# descending order, if we found one prime then it is the answer :) Blazing fast ! :)

from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

test_set = [7654321, 654321, 54321, 4321, 321, 21]

def solve():
    for x in test_set:
        s = str(x)
        for y in permutations(s):
            z = int(''.join(y))
            if is_prime(z):
                return z

print solve()
