# project euler problem 07
# http://projecteuler.net/problem=7

from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = count(2)
cnt = 0
for num in numbers:
    if is_prime(num):
        cnt += 1
    if cnt == 10001:
        print num
        break


