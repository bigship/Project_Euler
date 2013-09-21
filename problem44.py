# project euler problem 44
# http://projecteuler.net/problem=44

from itertools import combinations
from operator import add, sub

def pentagonal(n):
    return n*(3*n-1)/2

pentagonals = {pentagonal(n) for n in xrange(1, 3000)}
c = combinations(pentagonals, 2)
for p in c:
    if add(*p) in pentagonals and abs(sub(*p)) in pentagonals:
        print abs(sub(*p))

