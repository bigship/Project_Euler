# project euler problem 24
# http://projecteuler.net/problem=24

from itertools import permutations

def solve():
    p = permutations("0123456789")
    for index, value in enumerate(p, 1):
        if index == 1000000:
            return ''.join(value)

print solve()