# project euler problem 06
# http://projecteuler.net/problem=6

print sum(xrange(1,101))**2 - sum(x**2 for x in xrange(1, 101))