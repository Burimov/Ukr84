# -*- coding: utf-8 -*-

def make_sudoku(size):
    import random

    rows_number = size ** 2
    rows_len = size ** 2

    number_line = []
    for i in range(1, size ** 2 + 1):
        number_line.append(i)

    number_line = number_line * (size ** 2)

    row = []
    temp_row = []
    n = 0
    m = 0

    for j in range(1, size + 1):
        n = m
        for i in range(1, size + 1):
            temp_row = number_line[n:(size ** 2) + n]
            row.append(temp_row)
            n = n + size
        m += 1

    # for i in row:
    #     print i

    return row


print make_sudoku(1)
