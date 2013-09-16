# project euler problem 33
# http://projecteuler.net/problem=33

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    return b

denominator = []
numerator   = []

for a in xrange(11, 100):
    a_tens  = a / 10
    a_units = a % 10
    for b in xrange(11, 100):
        b_tens  = b / 10
        b_units = b % 10
        if a < b and a_units != 0:
            if a_tens == b_tens:
                if b_units * a == b * a_units:
                    numerator.append(a)
                    denominator.append(b)
            if a_tens == b_units:
                if b_tens * a == a_units * b:
                    numerator.append(a)
                    denominator.append(b)
            if a_units == b_tens:
                if a_tens * b == a * b_units:
                    numerator.append(a)
                    denominator.append(b)
            if a_units == b_units:
                if a_tens * b == a * b_tens:
                    numerator.append(a)
                    denominator.append(b)

print numerator, denominator 
print reduce(lambda x,y:x*y, denominator) / gcd(reduce(lambda x, y:x*y, numerator), reduce(lambda x,y:x*y, denominator))


