# project euler problem 51
# http://projecteuler.net/problem=51

# This is by far the most difficult problem that I met.
# Since we are looking for the smallest prime which can met the request, 
# the replaced digit must be 0, 1, or 2 otherwise we can't  make 8 different numbers.

from ProjectEulerUtils import is_prime

for i in xrange(100003, 1000000):
    if not is_prime(i):
        continue
    else:
        st = str(i)
        for j in '012':
            if st.count(j) > 1:
                cnt = 1
                for k in xrange(int(j)+1, 10):
                    tmp = st.replace(j, str(k))
                    if is_prime(int(tmp)):
                        cnt += 1
                    else:
                        continue
            else:
                continue
        if cnt == 8:
            print i
            break
