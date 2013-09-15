# project euler problem 26
# http://projecteuler.net/problem=26

# 1 % 7  = 1
# 10 % 7 = 3
# 30 % 7 = 2
# 20 % 7 = 6
# 60 % 7 = 4
# 40 % 7 = 5
# 50 % 7 = 1
# ... same pattern appears again
# recurring cycle length of 1 / 7  is 6
# the value that has the longest recurring cycle length must be a prime
cycle_length = []
def recurring_cycle_length(n):
    value = 1
    reminder = []
    while value % n != 0 and (value % n) not in reminder:
        reminder.append(value % n)
        value = 10 * (value % n)
    cycle_length.append(len(reminder))
    return len(reminder)

longest =  max(map(recurring_cycle_length, xrange(1, 1000)))
#print longest
# subscript starts from 0, we should plus one 
print cycle_length.index(longest) + 1

