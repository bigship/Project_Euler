# project euler problem 65
# http://projecteuler.net/problem=65

from ProjectEulerUtils import gcd

# x is numerator
# y is denominator
def f(n):
    if (n+1) % 3 == 0:
        x, y = 3, 2*(n+1)
    else:
        x, y = 1, 1

    for i in xrange(n-1, 0, -1):
        if (i+1) % 3 == 0:
            x, y = 3*y, 3*x+2*y*(1+i)
        else:
            x, y = y, x+y

    x, y = 2*y+x, y
    g = gcd(x, y)
    return x/g, y/g

print sum(map(int, str(f(99)[0])))
