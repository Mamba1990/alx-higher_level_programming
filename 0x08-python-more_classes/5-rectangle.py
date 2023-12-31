#!/usr/bin/python3
"""Represents a Rectangle class."""


class Rectangle:
    """Defining a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): the new rectangle's width.
            height (int): the new rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting/setting the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting/setting the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Displays the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Displays the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Dislpays the printable representation of the Rectangle.

        Returning the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for k in range(self.__height):
            [rec.append('#') for i in range(self.__width)]
            if k != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Returning the string representation of the Rectangle."""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """Displays a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
