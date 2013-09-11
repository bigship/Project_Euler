# project euler problem 01
# http://projecteuler.net/problem=1

print sum(x for x in xrange(1, 1000) if x % 3 == 0 or x % 5 == 0)