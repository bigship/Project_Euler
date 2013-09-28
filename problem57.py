# project euler problem 57
# http://projecteuler.net/problem=57

cnt = 0
a, b = 2, 1
for i in xrange(2, 1001):
    a, b = 2*a + b, a
    numerator = a+b
    denominator = a
    if len(str(numerator)) > len(str(denominator)):
        cnt += 1

print cnt