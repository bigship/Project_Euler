# project euler problem 45
# http://projecteuler.net/problem=45

def pentagon(limit=100000):
    for i in xrange(1, limit+1):
        yield i*(3*i-1)/2

def hexagonal(limit=100000):
    for i in xrange(1, limit+1):
        yield i*(2*i-1)

def triangle(limit=100000):
    for i in xrange(1, limit+1):
        yield i*(i+1)/2

s1 = set(pentagon())
s2 = set(hexagonal())
s3 = set(triangle())

print s1.intersection(s2.intersection(s3))