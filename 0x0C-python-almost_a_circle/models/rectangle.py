#!/usr/bin/python3
"""Represents a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new Rectangle.

        Args:
            width (int): the new Rectangle's width.
            height (int): the new Rectangle's height.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The new Rectangle'identity.
        Raises:
            TypeError: If either of width or height is not an integer.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Setting/getting the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setting/getting the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setting/getting the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Setting/getting the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Displays the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Displays the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for he in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wi in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the Rectangle.

        Args:
            *args (ints):the new attribute values.
                - first argument is the id attribute
                - second argument is the width attribute
                - thirth argument is the height attribute
                - fourth argument is the x attribute
                - fifth argument is the  y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ar == 1:
                    self.width = arg
                elif ar == 2:
                    self.height = arg
                elif ar == 3:
                    self.x = arg
                elif ar == 4:
                    self.y = arg
                ar += 1

        elif kwargs and len(kwargs) != 0:
            for j, v in kwargs.items():
                if j == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif j == "width":
                    self.width = v
                elif j == "height":
                    self.height = v
                elif j == "x":
                    self.x = v
                elif j == "y":
                    self.y = v

    def to_dictionary(self):
        """Displays the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Displays the print() and str() that represent the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
