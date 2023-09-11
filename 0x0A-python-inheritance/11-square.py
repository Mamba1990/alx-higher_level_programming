#!/usr/bin/python3
"""Represents a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size):
        """Initializing a new square.

        Args:
            size (int): new square's size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
