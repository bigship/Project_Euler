# project euler problem 59
# http://projecteuler.net/problem=59

from itertools import combinations, permutations

# use a valid char box
# they should appear in a English plain text the most often
# 'a-z' and 'A-Z' plus ' '(space)
valid_char = [32] + [x for x in xrange(65, 91)] + [x for x in xrange(97, 123)]

# read cipher text and build a list 
with open('cipher1.txt', 'r') as f:
    encrypted_data = map(int, f.read().split(','))

# brute force the password combinations
password_combinations = combinations('abcdefghijklmnopqrstuvwxyz', 3)

# possible password
canditate = None
maxcount = 0
for p in password_combinations:
    pc = ''.join(p)
    for pp in permutations(pc): 
        password = ''.join(pp)
        i = 0
        count = 0
        for e in encrypted_data:
            t = e ^ ord(password[i])
            if t in valid_char:
                count += 1
            i += 1
            if i == 3:
                i = 0
    
        if maxcount < count:
            maxcount = count
            canditate = password
        
print canditate, maxcount
