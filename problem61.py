# project euler problem 61
# http://projecteuler.net/problem=61
from itertools import permutations

triangle = [str(x*(x+1)/2) for x in xrange(1, 10000) if 1000 <= x*(x+1)/2 <= 9999]
square = [str(x**2) for x in xrange(1, 1000) if 1000 <= x**2 <= 9999]
pentagonal = [str(x*(3*x-1)/2) for x in xrange(1, 10000) if 1000 <= x*(3*x-1)/2 <= 9999]
hexagonal = [str(x*(2*x-1)) for x in xrange(1, 10000) if 1000 <= x*(2*x-1) <= 9999]
heptagonal = [str(x*(5*x-3)/2) for x in xrange(1, 10000) if 1000 <= x*(5*x-3)/2 <= 9999]
octagonal = [str(x*(3*x-2)) for x in xrange(1, 10000) if 1000 <= x*(3*x-2) <=9999]

sequence = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

def is_cyclic(a, b):
    return a[-2:] == b[:2]

def solve():
    for seq in permutations(sequence):
        for a in seq[0]:
            for b in seq[1]:
                if is_cyclic(a, b):
                    for c in seq[2]:
                        if is_cyclic(b, c):
                            for d in seq[3]:
                                if is_cyclic(c, d):
                                    for e in seq[4]:
                                        if is_cyclic(d, e):
                                            for f in seq[5]:
                                                if is_cyclic(e, f) and is_cyclic(f, a):
                                                    return sum(map(int, [a, b, c, d, e, f]))

print solve()
