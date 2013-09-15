# project euler problem 29
# http://projecteuler.net/problem=29

# Yet another one-liner :)
print len({a**b for a in xrange(2,101) for b in xrange(2, 101)})