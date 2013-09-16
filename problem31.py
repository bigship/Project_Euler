# project euler problem 31
# http://projecteuler.net/problem=31

# classic dynamic programming 

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0] * target

for coin in coins:
    for i in xrange(coin, target+1):
        ways[i] += ways[i - coin]
print ways[target]
