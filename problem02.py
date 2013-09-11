# project euler problem 02
# http://projecteuler.net/problem=2

def fibonacci(limit):
	a, b = 0, 1
	while b < limit:
		yield b
		a, b = b, a+b

print sum(x for x in fibonacci(4000000) if x % 2 == 0)