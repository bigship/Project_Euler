# project euler problem 04
# http://projecteuler.net/problem=4

print max(a*b for a in xrange(100, 1000) for b in xrange(100, 1000) if str(a*b) == str(a*b)[::-1])