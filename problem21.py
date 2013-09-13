# project euler problem 21
# http://projecteuler.net/problem=21

def divisors_sum(n):
    s = set()
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n/i)
    # numbers less than n which divide evenly into n
    # so remove n itself
    s.remove(n)
    return sum(s)

d = {}
for i in xrange(1, 10001):
    d[i] = divisors_sum(i)

print sum(x for x in xrange(1, 10001) if d.get(d[x]) == x and d[x] != x)
