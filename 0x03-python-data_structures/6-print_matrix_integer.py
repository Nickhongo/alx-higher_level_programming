#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(matrix) == 1 and len(row) == 0:
            print('')
            return
        for element in row:
            print("{:d}".format(element), end=" ")
            if row.index(element) == len(row) -1:
                print('\n', end='')
                continue
            print(" ", end='')
