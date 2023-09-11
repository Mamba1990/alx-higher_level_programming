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

    def area(self):
        """Displays the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Displays the print() and str() representation of a Rectangle."""
        strr = "[" + str(self.__class__.__name__) + "] "
        strr += str(self.__width) + "/" + str(self.__height)
        return strr
