#!/usr/bin/python3
"""Represents a Pascal's Triangle function."""


def pascal_triangle(n):
    """Defines Pascal's Triangle of size n.

    Displays a list of lists of integers that represent the triangle.
    """
    if n <= 0:
        return []

    _triangles = [[1]]
    while len(_triangles) != n:
        ttri = _triangles[-1]
        ttmp = [1]
        for k in range(len(ttri) - 1):
            ttmp.append(ttri[k] + ttri[k + 1])
        ttmp.append(1)
        _triangles.append(ttmp)
    return _triangles
