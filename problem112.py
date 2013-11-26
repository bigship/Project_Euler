# -*- encoding: utf-8 -*-
# project euler problem 112
# http://projecteuler.net/problem=112

import itertools

def isBouncy(n):
    st = str(n)
    length = len(st)
    prev_state = None
    current_state = None
    
    if length <= 2:
        return False
    
    # Initialize state
    # increase == 1
    # decrease == 2
    # equal    == 3
    if st[0] < st[1]:
        prev_state = current_state = 1
    elif st[0] > st[1]:
        prev_state = current_state = 2
    else:
        prev_state = current_state = 3
    
    i = 1
    while i < length - 1:
        if st[i] < st[i+1]:
            current_state = 1
            if prev_state == 2:
                return True
            else:
                prev_state = current_state
        elif st[i] > st[i+1]:
            current_state = 2
            if prev_state == 1:
                return True
            else:
                prev_state = current_state
        else:
            current_state = 3
            if prev_state != 3:
                pass
            else:
                prev_state = current_state
        i += 1
    
    return False

count = 0
for n in itertools.count(101):
    if isBouncy(n):
        count += 1
    
    if 100*count == 99*n:
        print n
        break
