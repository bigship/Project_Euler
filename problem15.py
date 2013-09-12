# project euler problem 15
# http://projecteuler.net/problem=15

# Solve this problem using combinatorics.
# All paths can be described as a series of directions. And since we can only go down
# and right, we could describe the path as a series of Ds and Rs.
# In the example 2x2 grid, all path can be described as:
# 1)DDRR 2)DRDR 3)DRRD 4)RDRD 5)RDDR 6)RRDD

# Based on the example, we can see that all paths have exactly 2N of which there are N Rs 
# and N Ds. So the solution is clear now: how many ways can we choose N out of 2N possible 
# places if the order doesn't matter ?
# the answer = (2N)! / N!*N!

from math import factorial
print factorial(40) / factorial(20) / factorial(20)
