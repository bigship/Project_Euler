# project euler problem 28
# http://projecteuler.net/problem=28

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is 
formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''
# The numbers on the 4 corners can be described as follows:
# top left     : (2n+1)^2 - 2n
# top right    : (2n+1)^2 
# bottom left  : (2n+1)^2 - 4n
# bottom right : (2n+1)^2 - 6n
# don't forget the 1 on the center

print sum(map(lambda x:4*(2*x+1)**2-12*x, xrange(1, (1001-5)/2+2+1))) + 1  