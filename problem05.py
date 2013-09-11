# project euler problem 05
# http://projecteuler.net/problem=5

# brute force, 45.8s on my computer
'''
import itertools

numbers = itertools.count(2520, 10)
for num in numbers:
	if all(num % i == 0 for i in xrange(1, 21)):
		print num
		break
'''
# much more efficent way, the answer is lcm(1..20) 
# runs at millisecond level
# functional programming 
def gcd(a, b):
	if a < b:
		a, b = b, a
	while a % b != 0:
		a, b = b, a%b
	return b

def lcm(a, b):
	return a*b / gcd(a, b)

print reduce(lcm, xrange(1, 21))

