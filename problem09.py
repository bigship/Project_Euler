# project euler problem 09
# http://projecteuler.net/problem=9

# burte force
def solve():
	for a in xrange(3, 1000):
		for b in xrange(4, 1000):
			if 1000*(a+b) - a*b == 500000:
				c = 1000 - a - b
				return a*b*c

print solve()
