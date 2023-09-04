#!/usr/bin/python3
"""Represents a Rectangle class."""


class Rectangle:
    """Defining a rectangle.

    Attributes:
        number_of_instances (int): The Rectangle instances' number.
        print_symbol (any): symbol used to represent a string .
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): the new rectangle's width.
            height (int): the new rectangle's height.
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Displays the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The 1st Rectangle.
            rect_2 (Rectangle): The nd Rectangle.
        Raises:
            TypeError: If none of rect_1 or rect_2 is a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Represnets the printable representation of the Rectangle.

        Displays the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for k in range(self.__height):
            [rec.append(str(self.print_symbol)) for i in range(self.__width)]
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
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
