# -*- encoding: utf-8 -*-
# project euler problem 72
# http://projecteuler.net/problem=72

def P(L):
    phi = range(L+1)
    for n in range(2, L+1):
        if phi[n] == n:
            for k in range(n, L+1, n):
                phi[k] -= phi[k] // n
    return sum(phi) - 1

print "Project Euler 72 Solution =", P(1000000)


