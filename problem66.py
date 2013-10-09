# project euler problem 66
# http://projecteuler.net/problem=66
# using continued fractions to solve Pell's equation
# check problem64, basically they are the same

ret = 0
pmax = 0

for D in xrange(2, 1001):
    limit = int(D ** 0.5)
    if limit ** 2 == D:
        continue

    m, d, a = 0, 1, limit
    numm1 = 1
    num = a
    denm1 = 0
    den = 1

    while num ** 2 - D * (den ** 2) != 1:
        m = d * a - m
        d = (D - m * m) / d
        a = (limit + m ) / d
        numm2 = numm1
        numm1 = num
        denm2 = denm1
        denm1 = den

        num = a*numm1 + numm2
        den = a * denm1 + denm2

    if num > pmax:
        pmax = num
        result = D

print result



