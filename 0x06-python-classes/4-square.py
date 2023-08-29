#!/usr/bin/python3

"""Defines a class of Square."""


class Square:
    """Definig a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int):  size of a new square.
        """
        self.size = size

    @property
    def size(self):
        """Getting/setting the currenit size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the current area of the square."""
        return (self.__size * self.__size)
