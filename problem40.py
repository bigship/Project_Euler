# project euler problem 40
# http://projecteuler.net/problem=40

# 1000000 = (9+90*2+900*3+9000*4+90000*5+6*x)
# x = 85185 .. 
# So we only need to iterate up to 100000 + 85186 = 185186 

s = ''
for i in xrange(1, 185187):
    s += str(i)

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])