#!/usr/bin/python3
"""Represents the class  Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing new instances.

        Args:
            width (int): The new Rectangle's width.
            height (int): The new Rectangle's height.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The new Rectangle's identity.
        Raises:
            TypeError: If none of width or height is an int.
            ValueError: If either width or height <= 0.
            TypeError: none of x or y is not an int.
            ValueError: either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width's getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width's setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height's getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height's setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x's getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x's setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y's getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y's setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Computes the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """Displays a rectangle """
        rectangle = self.y * "\n"
        for k in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """The special method of a string """
        strRectangle = "[Rectangle] "
        strId = "({}) ".format(self.id)
        strXy = "{}/{} - ".format(self.x, self.y)
        strWh = "{}/{}".format(self.width, self.height)

        return strRectangle + strId + strXy + strWh

    def update(self, *args, **kwargs):
        """ updates the rectangle.

        Args:
            *args (ints):th values of the new attribute.
                - first argument is the id attribute
                - second argument is the width attribute
                - thirth argument is the height attribute
                - fourth argument is the x attribute
                - fifth argument is the y attribute
            **kwargs (dict): key/value pairing of attributes.
        """
        if args is not None and len(args) is not 0:
            listAtr = ['id', 'width', 'height', 'x', 'y']
            for k in range(len(args)):
                setattr(self, listAtr[k], args[k])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Displays a dictionary with properties """
        listAtr = ['id', 'width', 'height', 'x', 'y']
        dictRes = {}

        for key in listAtr:
            dictRes[key] = getattr(self, key)

        return dictRes
