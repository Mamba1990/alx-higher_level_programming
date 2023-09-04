#!/usr/bin/python3
"""Represents a function that prints a square ."""


def print_square(size):
    """Displays a square with #.

    Args:
        size (int): square's height/width of the square.
    Raises:
        TypeError:  size is not an integer.
        ValueError:  size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for k in range(size):
        [print("#", end="") for k in range(size)]
        print("")
