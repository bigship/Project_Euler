# project euler problem 48
# http://projecteuler.net/problem=48

# one-liner :)
print sum(map(lambda x:x**x, xrange(1, 1001))) % 10**10

print reduce(lambda x,y:x+y, (z**z for z in xrange(1, 1001))) % 10**10