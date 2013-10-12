# -*- encoding: utf-8 -*-
# project euler problem 96
# http://projecteuler.net/problem=96

# Su Doku
grid = [[[0 for i in range(9)] for i in range(9)] for i in range(50)]
with open('sudoku.txt', 'r') as f:
    lines = f.readlines()
    for line_number, line in enumerate(lines, 1):
        # omit this line, it is not data
        if line_number % 10 == 1:
            continue
        else:
            for col, digit in enumerate(line[:-1]):
                if line_number % 10 == 0:
                    x = line_number / 10 - 1
                    y = 8
                else:
                    x = line_number / 10
                    y = line_number % 10 - 2
                grid[x][y][col] = int(digit)

