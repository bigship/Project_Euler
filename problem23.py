# project euler problem 23
# http://projecteuler.net/problem=23

# brute force, finished in 13.1s on my computer. Need to optimize
# Is it possible to avoid computing the abundant numbers in the first place ?
# NOTE: using generators instead of lists can save some CPU time. 

from itertools import combinations_with_replacement as cr

END = 28123

def is_abundant(n):
    s = set()
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n/i)
    s.remove(n)
    return sum(s) > n

nums = [False] * END
abundant_numbers = (x for x in xrange(1, END) if is_abundant(x))
sieve = (sum(i) for i in cr(abundant_numbers, 2) if sum(i) < END)

for i in sieve:
    nums[i] = True

print sum(i for i in xrange(1, END) if not nums[i])
