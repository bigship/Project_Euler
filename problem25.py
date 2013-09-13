# project euler problem 25
# http://projecteuler.net/problem=25

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

def solve():
    for index, value in enumerate(fibonacci(), 1):
        if len(str(value)) == 1000:
            return index

print solve()            


