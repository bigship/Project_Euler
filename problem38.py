# project euler problem 38
# http://projecteuler.net/problem=38
# We can easily get that 5-digit number can not meet the request
# So only need to test all the numbers less than 10000. 
# My solution finished in 0.2s

ret = []
for x in xrange(1, 10000):
    t = ''
    for n in xrange(1, 10):
        t += str(x*n)
        if len(t) == 9 and ''.join(sorted(t)) == '123456789':
            ret.append(int(t))
            break

print max(ret)
