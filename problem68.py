# project euler problem 68
# http://projecteuler.net/problem=68

from itertools import permutations

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maxvalue = 0

def is_valid_list(lst):
    # starting from the group of three with the numerically lowest external node
    if lst[0] != min([lst[0], lst[3], lst[5], lst[7], lst[9]]):
        return False

    # 10 can't be in the inner-ring, otherwise we can't form a 16-digit string
    if lst[1] == 10 or lst[2] == 10 or lst[4] == 10 or lst[6] == 10 or lst[8] == 10:
        return False

    # check each line 
    if lst[0] + lst[1] + lst[2] !=  lst[3] + lst[2] + lst[4]:
        return False

    if lst[0] + lst[1] + lst[2] != lst[5] + lst[4] + lst[6]:
        return False

    if lst[0] + lst[1] + lst[2] != lst[7] + lst[6] + lst[8]:
        return False

    if lst[0] + lst[1] + lst[2] != lst[9] + lst[8] + lst[1]:
        return False

    return True

for n in permutations(seq):
    if is_valid_list(n):
        catstring = (str(n[0]) + str(n[1]) + str(n[2]) + 
                     str(n[3]) + str(n[2]) + str(n[4]) + 
                     str(n[5]) + str(n[4]) + str(n[6]) + 
                     str(n[7]) + str(n[6]) + str(n[8]) + 
                     str(n[9]) + str(n[8]) + str(n[1]))
        
        temp = int(catstring)
        if temp > maxvalue:
            maxvalue = temp

print maxvalue 

