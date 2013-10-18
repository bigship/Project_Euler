# -*- encoding: utf-8 -*-
# project euler problem 85
# http://projecteuler.net/problem=85

# For a particular rectangle that has the width a and height b, 
# we can count the number of grids in this way:  ((a+1)*a / 2) * ((b+1)*b/2) 
# if you think of the rectangle in a rectangular coordinate system

LIMIT = 2000000
def count(n):
    return n*(n-1) / 2

min = 1000000000  # set for a large number
a, b = 0, 0
for x in xrange(1, 100):
    for y in xrange(1, 100):
        rectangle_cnt = count(x+1) * count(y+1)
        t = abs(rectangle_cnt - LIMIT)
        if min > t:
            min = t
            a, b = x, y

print a, b, a*b, count(a+1)*count(b+1) 