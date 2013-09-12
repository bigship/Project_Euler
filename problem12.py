# project euler problem 12
# http://projecteuler.net/problem=12
# burte force, 5.9s on my computer

from itertools import count

def get_divisors(n):
    s = set()
    for i in xrange(1, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n/i)
    return s

for x in count(8):
    triangle_num = sum(xrange(x))
    if len(get_divisors(triangle_num)) > 500:
        print triangle_num, x
        break