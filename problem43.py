# project euler problem 43
# http://projecteuler.net/problem=43

import itertools

def generate_subnumber(n):
    s = str(n)
    for i in xrange(1, 8):
        yield int(s[i:i+3])

total_sum = 0
prime_divisor = [2, 3, 5, 7, 11, 13, 17]
for numbers in itertools.permutations('1234567890'):
    s = ''.join(numbers)
    if s[0] != '0':
        num = int(s)
        flag = True
        for index, sub in enumerate(generate_subnumber(num)):
            if sub % prime_divisor[index] != 0:
                flag = False
                break
        if flag:
            total_sum += num 

print total_sum

