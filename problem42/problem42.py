# project euler problem 42
# http://projecteuler.net/problem=42

def is_triangle_number(n):
    t = int((2*n)**0.5)
    if t*(t+1)/2 != n:
        return False
    else:
        return True

total_cnt = 0
with open('words.txt', 'r') as f:
    words = f.read().split(',')
    for word in words:
        word_value = sum(map(lambda x:ord(x)-64, word.replace('"', '')))
        if is_triangle_number(word_value):
            total_cnt += 1

print total_cnt

