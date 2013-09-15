# project euler problem 30
# http://projecteuler.net/problem=30

# Since 9**5*7 = 413343 is a 6-digit number
# so there is no 7-digit number can fullfil the request
# hence, we can determine the upper-bond. 
# Finished in 7.0s on my computer

total_sum = 0
for x in xrange(2, 1000000):
    if x == sum(map(lambda x:x**5, map(int, str(x)))):
        total_sum += x
print total_sum
