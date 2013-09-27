# project euler problem 56
# http://projecteuler.net/problem=56
# Yet another one-liner 
print max([sum(map(int, str(a**b))) for a in xrange(1, 101) for b in xrange(1, 101)])