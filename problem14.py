# project euler problem 14
# http://projecteuler.net/problem=14

def collatz_len(n):
    global cached

    cnt = 0
    i = n
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        cnt += 1
        if n in cached:
            cached[i] = cnt + cached[n]
            return cnt + cached[n] 
    return cnt + 1

cached = {13:10, 40:9, 20:8, 10:7, 5:6, 16:5, 8:4, 4:3, 2:2, 1:1}

ans = 0
longest = 0
for x in xrange(13, 1000001):
    tmp = collatz_len(x)
    if tmp > longest:
        longest = tmp
        ans = x

print ans, longest


