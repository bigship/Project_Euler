# project euler problem 52
# http://projecteuler.net/problem=52

def sort_string(n):
    st = str(n)
    return ''.join(sorted(st))

for i in xrange(123456, 165432):
    x2 = sort_string(i*2)
    x3 = sort_string(i*3)
    if x2 != x3:
        continue
    else:
        x4 = sort_string(i*4)
        if x3 != x4:
            continue
        else:
            x5 = sort_string(i*5)
            if x4 != x5:
                continue
            else:
                x6 = sort_string(i*6)
                if x5 != x6:
                    continue
                else:
                    print i
                    break
