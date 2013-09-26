# project euler problem 55
# http://projecteuler.net/problem=55

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychre(n):
    s = str(n)
    t = n + int(s[::-1])
    cnt = 1
    while not is_palindrome(t):
        t += int(str(t)[::-1])
        cnt += 1
        if cnt == 50:
            return True
    return False

print sum(1 for x in xrange(1, 10001) if is_lychre(x))