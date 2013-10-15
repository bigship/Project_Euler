# -*- encoding: utf-8 -*-
# project euler problem 71
# http://projecteuler.net/problem=71

# p / q < 3 / 7
# p < 3*q / 7
# p <= 3*q / 7 - 1

d = {}
for q in xrange(2, 1000000):
    p = 3*q/7 - 1
    d[p] = (q, float(p) / q)

ret = sorted(d.items(), key=lambda item:item[1][1], reverse=True)
print ret[0]
