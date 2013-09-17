# project euler problem 36
# http://projecteuler.net/problem=36

LIMIT = 1000000

def is_palindromic(n):
    s = str(n)
    return s == s[::-1]

total_sum = 0
for x in xrange(1, LIMIT):
    if is_palindromic(x) and is_palindromic(bin(x)[2:]):
        total_sum += x

print total_sum