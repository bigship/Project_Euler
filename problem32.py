# project euler problem 32
# http://projecteuler.net/problem=32

s = set()
for a in xrange(1, 100):
    if a % 10 == 0:
        continue
    for b in xrange(101, 10000):
        if b % 10 == 0:
            continue
        if ''.join(sorted(''.join(str(a) + str(b) + str(a*b)))) == '123456789':
            s.add(a*b)

print sum(s)
