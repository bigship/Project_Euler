# project euler problem 17
# http://projecteuler.net/problem=17

d = {
    1:'one', 2:'two', 3:'three', 4:'four',
    5:'five', 6:'six', 7:'seven', 8:'eight',
    9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
    13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
    17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
    30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
    70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred',
    0:''
}

def letters_for_number(n):
    global d

    if n < 100:
        if n in d:
            return d[n]
        else:
            return d[n/10*10] + d[n%10]

    hundred = n / 100
    tens = n % 100 / 10
    units = n % 10

    if tens == 0 and units == 0: 
        return d[hundred] + d[100]

    p = tens * 10 + units
    if p in d:
        return d[hundred] + d[100] + 'and' + d[p]
    else:
        return d[hundred] + d[100] + 'and' + d[tens*10] + d[units]  

print sum(map(len, map(letters_for_number, xrange(1, 1000)))) + len('onethousand')



