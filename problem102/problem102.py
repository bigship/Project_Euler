# -*- encoding: utf-8 -*-
# project euler problem 102
# http://projecteuler.net/problem=102

# first try, brute force, it took about 100 seconds, way too slow.
import time, itertools

start = time.time()
maxl = []
for a in xrange(3, 1001):
    l = []
    head = ((a+1) + (a-1)) % (a**2)
    l.append(head)
    for n in itertools.count(2):
        r = ((a+1)**n + (a-1)**n) % (a**2)
        if head != r:
            l.append(r)
        else:
            maxl.append(max(l))
            break

print sum(maxl)
end = time.time() - start
print 'It took %f seconds.' % end

# 'a' and 'rmax' has the following relationship:
# a     3x2   4x2   5x4    6x4    7x6    8x6    9x8    10x8
# rmax   6     8    20     24     42     48     72      80
# easy one-liner code now, only took 0.000279 seconds :)
print sum(a*n for a, n in zip(xrange(3, 1000, 2), xrange(2, 1000, 2))) + sum(a*n for a, n in zip(xrange(4, 1002, 2), xrange(2, 1000, 2)))