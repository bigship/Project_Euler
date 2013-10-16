# -*- encoding: utf-8 -*-
# project euler problem 99
# http://projecteuler.net/problem=99
import math

with open('base_exp.txt', 'r') as f:
    data = f.read().split('\n')

largest = 0
for pair in data:
    t = pair.split(',')
    tmp = int(t[1]) * math.log10(int(t[0]))
    if largest < tmp:
        largest = tmp
        p = pair

print data.index(p) + 1
