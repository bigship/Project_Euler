import time, decimal

start = time.time()
decimal.getcontext().prec = 102

square = [x**2 for x in xrange(1, 100) if x**2 <= 100]

def Sum(n):
    st = str(n).replace('.', '')
    return sum(map(int, st[0:100]))

totalsum = 0
for i in xrange(1, 101):
    if i not in square:
        totalsum += Sum(decimal.Decimal(i).sqrt())
        
print totalsum
end = time.time() - start
print "It took %f seconds" % end