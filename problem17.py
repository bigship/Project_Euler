# project euler problem 17
# http://projecteuler.net/problem=17

d = {
    1:len('one'), 2:len('two'), 3:len('three'), 4:len('four'),
    5:len('five'), 6:len('six'), 7:len('seven'), 8:len('eight'),
    9:len('nine'), 10:len('ten'), 11:len('eleven'), 12:len('twelve'),
    13:len('thirteen'), 14:len('fourteen'), 15:len('fifteen'), 16:len('sixteen'),
    17:len('seventeen'), 18:len('eighteen'), 19:len('nineteen'), 20:len('twenty') ,
    30:len('thirty'), 40:len('forty'), 50:len('fifty'), 60:len('sixty'),
    70:len('seventy'), 80:len('eighty'), 90:len('ninty'), 100:len('hundred')
}

def letters_length(n):
    global d

    if 1 <= n <= 20:
        return d[n]

    if  21 <= n <= 99:
        return d[(n/10)*10] + d[n - (n/10)*10]

print letters_length(34)  