# project euler problem 18
# http://projecteuler.net/problem=18

# two methods: brute force and dynamic programming.
# problem18 can solve by a brute force way, since the dataset
# are not too large. But with large data set, dynamic programming
# is the classic way to do

data_set = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 04, 82, 47, 65],
    [19, 01, 23, 75, 03, 34],
    [88, 02, 77, 73, 07, 63, 67],
    [99, 65, 04, 28, 06, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
]

def brute_force():
    total_possible_route = 2 ** (len(data_set) - 1)
    max_val = 0
    for i in xrange(0, total_possible_route):
        temp_sum, index = data_set[0][0], 0
        for j in xrange(0, len(data_set) - 1):
            index = index + (i >> j & 1)
            temp_sum += data_set[j+1][index]
        if temp_sum > max_val:
            max_val = temp_sum

    return max_val


def dynamic_programming():
    total_lines = len(data_set)
    for i in xrange(total_lines - 2, -1, -1):
        for j in xrange(0, i+1):
            data_set[i][j] += max(data_set[i+1][j], data_set[i+1][j+1])

    return data_set[0][0]

if __name__ == '__main__':
    #print brute_force()
    print dynamic_programming()
