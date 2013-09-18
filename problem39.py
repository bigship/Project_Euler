# project euler problem 39
# http://projecteuler.net/problem=39
# Too damn slow !! 

def solution_amount(n):
    cnt = 0
    for a in xrange(1, n):
        for b in xrange(a+1, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                cnt += 1
    return cnt

max_solutions = 0
ret = 0
for p in xrange(12, 1000):
    tmp = solution_amount(p)
    if tmp > max_solutions:
        max_solutions = tmp
        ret = p

print ret, max_solutions
