# project euler problem 63
# http://projecteuler.net/problem=63

import time

start = time.time()
# determine the upper-limit of exponent
upper_limit = 1
while True:
    if len(str(9**upper_limit)) < upper_limit:
        break
    else:
        upper_limit += 1

count = 0
for m in xrange(1, 10):
    for n in xrange(1, upper_limit):
        if len(str(m**n)) == n:
            count += 1

print count, upper_limit
end = time.time() - start
print 'It took %f seconds' % end
