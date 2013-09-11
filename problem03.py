# project euler problem 03
# http://projecteuler.net/problem=3

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print max(x for x in xrange(2, int(600851475143 ** 0.5) + 1) if 600851475143 % x == 0 and is_prime(x))



