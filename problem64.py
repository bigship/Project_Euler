# project euler problem 64
# http://projecteuler.net/problem=64
# check http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

upperbound = 10000
cnt = 0

for n in xrange(2, upperbound + 1):
    limit = int(n**0.5)
    if limit ** 2 == n:
        continue

    period = 0
    d = 1
    m = 0
    a = limit

    m = d*a - m
    d = (n - m**2) / d
    a = (limit + m) / d
    period += 1

    while a != 2*limit:
        m = d*a - m
        d = (n - m**2) / d
        a = (limit + m) / d
        period += 1

    if period % 2 == 1:
        cnt += 1

print cnt 