# project euler problem 34
# http://projecteuler.net/problem=34

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

d = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def digits_fact_sum(n):
    ret = 0
    s = str(n)
    for i in s:
        ret += d[int(i)]
    return ret

total_sum = 0
for x in xrange(10, 2540160):
    s = digits_fact_sum(x)
    if s == x:
        total_sum += x
print total_sum
