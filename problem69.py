# project euler problem 69
# http://projecteuler.net/problem=69

# if n has the factor 2 every 2nd number will not be relatively prime to n
# if n has the factor 3 every 3rd number will not be relatively prime to n
# and so on....
# for phi(n) to be as small as posible to make n/phi(n) maximal 
# it would be very nice if every 2nd, 3rd and 5th... number would not be relatively prime to n

from ProjectEulerUtils import prime_sieve, gcd, is_prime

def phi(n):
    cnt = 0
    if is_prime(n):
        return n - 1
    for i in xrange(2, n-1):
        if gcd(i, n) == 1:
            cnt += 1
    return cnt + 2

primes = prime_sieve(1000)
ret = 1
for i in primes:
    ret = ret * i
    if ret >= 1000000:
        print ret / i
        break
