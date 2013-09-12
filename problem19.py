# project euler problem 19
# http://projecteuler.net/problem=19
# We can solve this problem by using standard library calendar
# piece of cake :)

import calendar

count = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if calendar.SUNDAY == calendar.weekday(year, month, 1):
            count += 1

print count

# Yet another crazy one-liner :)
print [calendar.SUNDAY == calendar.weekday(year, month, 1) for year in xrange(1901, 2001) for month in xrange(1, 13)].count(True)
print sum([1 for year in xrange(1901, 2001) for month in xrange(1, 13) if calendar.SUNDAY == calendar.weekday(year, month, 1)])
