# project euler problem 27
# http://projecteuler.net/problem=27
# brute force. Finished in 7.3s.
# Any better way to solve ?

from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

max_length = 0
product = 0
reta = 0
retb = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        length = 0
        for n in count(0):
            if is_prime(n**2 + a*n + b):
                length += 1
            else:
                break
        if length > max_length:
            max_length = length
            reta = a
            retb = b
            product = a*b

print product, reta, retb

