# project euler problem 50
# http://projecteuler.net/problem=50
# The sum of the prime numbers less than 4000 are 1013507, a little bit more than one million,
# so we only need to compute prime numbers below 4000. 

from ProjectEulerUtils import prime_sieve, is_prime

max_length = 0
index_start, index_end = 0, 0
prime_table = [x for x in prime_sieve(4000)]
for start in xrange(0, len(prime_table)):
    for end in xrange(len(prime_table)-1, start, -1):
        total_sum = sum(prime_table[start:end+1])
        if total_sum <= 1000000 and is_prime(total_sum):
            length = end - start + 1
            if max_length < length:
                max_length = length
                index_start, index_end = start, end
            break

print sum(prime_table[index_start:index_end+1]), max_length, index_start, index_end