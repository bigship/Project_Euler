# -*- encoding: utf-8 -*-
# project euler problem 92
# http://projecteuler.net/problem=92

import time

def transform(n):
    total = 0
    while n:
        total += (n%10)**2
        n //= 10
    return total

start = time.time()
set1 = set([1])
set2 = set([89, 145, 42, 20, 4, 16, 37, 58])

for n in xrange(1, 568):
    ds = transform(n)
    while ds not in set1 and ds not in set2:
        ds = transform(ds)
    if ds in set1:
        set1.add(n)
    else:
        set2.add(n)
        
count = 0
for i in xrange(1, 10000000):
    t = i
    while True:
        if t in set2:
            count += 1
            break
        elif t in set1:
            break 
        else:
            t = transform(t)

print count
end = time.time() - start
print 'It took %f seconds' % end