# project euler problem 62
# http://projecteuler.net/problem=62

cubeTable = [x**3 for x in xrange(345, 10000)]
seq = map(lambda x:''.join(sorted(str(x))), cubeTable)

for x in cubeTable:
    st = ''.join(sorted(str(x)))
    if seq.count(st) == 5:
        print x
        break
