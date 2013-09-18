# project euler problem 37
# http://projecteuler.net/problem=37

# Depending on the problem description, we knew that there is only 11 primes that are both 
# truncatable from left to right and right to left. So we can set the TOTAL_COUNT as 11,
# and use it as the loop break condition. (Don't know how to prove it)
# But what really interests me is how can we determine the upper-bond of the prime number ?
# My solution just set the prime upper-bond as one million, it works but not that great.

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def truncat_num(n):
    s = str(n)
    for i in xrange(0, len(s)):
        yield int(s[i:])
        yield int(s[0:i+1])

TOTAL_COUNT = 11
last_digit_sieve = [0, 1, 2, 4, 5, 6, 8, 9]
first_digit_sieve = [1, 4, 6, 8, 9]

cnt = 0
total_sum = 0
for n in xrange(23, 1000000):
    s = str(n)
    first_digit = int(s[0])
    last_digit = int(s[-1])
    if first_digit in first_digit_sieve or \
    last_digit in last_digit_sieve:
        continue

    if all(is_prime(x) for x in truncat_num(n)):
        total_sum += n
        cnt += 1
        if cnt == TOTAL_COUNT:
            break

print total_sum
