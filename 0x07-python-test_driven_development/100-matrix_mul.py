#!/usr/bin/python3
"""Represents a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The 1st matrix.
        m_b (list of lists of ints/floats): The 2nd matrix.
    Raises:
        TypeError: If none of m_a or m_b is a list of lists of ints/floats.
        TypeError: If none of m_a or m_b is not empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If none of m_a and m_b can be multiplied.
    Returns:
        New matrix that represents the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(el, int) or isinstance(el, float))
               for el in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(el, int) or isinstance(el, float))
               for el in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invertedB = []
    for rr in range(len(m_b[0])):
        newRow = []
        for d in range(len(m_b)):
            newRow.append(m_b[d][rr])
        invertedB.append(newRow)

    newMatrix = []
    for row in m_a:
        newRow = []
        for colm in invertedB:
            _prod = 0
            for j in range(len(invertedB[0])):
                _prod += row[j] * colm[j]
            newRow.append(_prod)
        newMatrix.append(newRow)

    return newMatrix
