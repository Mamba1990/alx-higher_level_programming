#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for k in range(len(row)):
            if k == len(row) - 1:
                print("{:d}".format(row[k]), end="")
            else:
                print("{:d}".format(row[k]), end=" ")
        print()
