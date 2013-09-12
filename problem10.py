# project euler problem 10
# http://projecteuler.net/problem=10

def prime_sieve(n):
	initSieve = []
	maxNum = int(n**0.5)+1
	for i in xrange(2, n):
		initSieve.append(True)
	j = 2
	while j <= maxNum:
		if initSieve[j-2]:
			for k in xrange(j*j, n, j):
				initSieve[k-2] = False
		j += 1
	output = (x+2 for x in xrange(len(initSieve)) if initSieve[x])
	return output

print sum(prime_sieve(2000000))
