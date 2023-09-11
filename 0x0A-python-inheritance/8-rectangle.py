#!/usr/bin/python3
"""Represents a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializing a new Rectangle.

        Args:
            width (int): new Rectangle's width.
            height (int): new Rectangle's height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
