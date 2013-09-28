# project euler problem 58
# http://projecteuler.net/problem=58

from itertools import count
from ProjectEulerUtils import is_prime

prime_cnt = 8
total_number = 13
# start from level 4
for i in count(4):
    if is_prime((2*i+1)**2-6*i):
        prime_cnt += 1
    if is_prime((2*i+1)**2-4*i):
        prime_cnt += 1
    if is_prime((2*i+1)**2-2*i):
        prime_cnt += 1
    total_number = (2*i+1)*2 - 1
    if prime_cnt * 100 <= 10 * total_number:
        print i*2 + 1
        break