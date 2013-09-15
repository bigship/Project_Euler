# project euler problem 30
# http://projecteuler.net/problem=30

# Since 9**5*7 = 413343 is a 6-digit number
# so there is no 7-digit number can fullfil the request
# hence, we can determine the upper-bond. 
# Finished in 7.0s on my computer.

total_sum = 0
for x in xrange(2, 1000000):
    if x == sum(map(lambda x:x**5, map(int, str(x)))):
        total_sum += x
print total_sum

# The equivalent C code only need 0.257s...
# Huge performance difference
'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned int get_sum(const char *s)
{
    unsigned int n = 0;
    unsigned int sum = 0;
    const char *p = s;
    while (*p != '\0') {
        n = *p - '0';
        sum += (n*n*n*n*n);
        p++;
    }
    return sum;
}

int main(int argc, char *argv[])
{
    unsigned int i = 0;
    char buffer[7] = {0};
    unsigned int ret = 0;

    for (i = 2; i < 1000000; i++) {
        sprintf(buffer, "%u", i);
        if (i == get_sum(buffer))
            ret += i;
    }

    printf("ret = %u\n", ret);
    return 0;
}
'''
