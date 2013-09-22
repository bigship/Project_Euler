# project euler problem 46
# http://projecteuler.net/problem=46

from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def test_goldbach(n):
    root = 1
    while n - 2*root**2 >= 2:
        if is_prime(n - 2*root**2):
            return True
        else:
            root += 1
    return False

def solve():            
    for ret in count(35, 2):
        if not is_prime(ret):
            if not test_goldbach(ret):
                return ret

print solve()
