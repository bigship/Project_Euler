# project euler problem 67
# http://projecteuler.net/problem=67

# Same problem as problem 18, this time with a very large dataset.
# It is a classic dynamic programming problem.

data_set = []

def get_data_set():
    global data_set
    with open('triangle.txt', 'r') as f:
        raw_data = f.read().split('\n')
        for line in raw_data:
            try:
                data_set.append(map(int, line.split(' ')))
            except ValueError:
                pass
    return data_set

data_set = get_data_set()
lines = len(data_set)
for i in xrange(lines - 2, -1, -1):
    for j in xrange(0, i+1):
        data_set[i][j] += max(data_set[i+1][j], data_set[i+1][j+1])

print data_set[0][0]
