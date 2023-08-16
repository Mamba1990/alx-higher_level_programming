#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    computes the square
    value of all integers of a matrix.
    """
    newMatrix = []
    for _col in matrix:
        square = list(map(lambda x: x**2, _col))
        newMatrix.append(square)
    return newMatrix
