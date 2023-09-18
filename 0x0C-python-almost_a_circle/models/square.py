#!/usr/bin/python3
""" Represents Square class,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing new instances

        Args:
            size (int): The new Square's size.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The new Square's identity.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines the special method of a string """
        strSquare = "[Square] "
        strId = "({}) ".format(self.id)
        strXy = "{}/{} - ".format(self.x, self.y)
        strWh = "{}/{}".format(self.width, self.height)

        return strSquare + strId + strXy + strWh

    @property
    def size(self):
        """ Defines Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """Defines Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """Defines the special method of a string """
        strRectangle = "[Square] "
        strId = "({}) ".format(self.id)
        strXy = "{}/{} - ".format(self.x, self.y)
        strSize = "{}".format(self.size)

        return strRectangle + strId + strXy + strSize

    def update(self, *args, **kwargs):
        """ updates the square """
        if args != None and len(args) != 0:
            listAtr = ['id', 'size', 'x', 'y']
            for k in range(len(args)):
                if listAtr[k] == 'size':
                    setattr(self, 'width', args[k])
                    setattr(self, 'height', args[k])
                else:
                    setattr(self, listAtr[k], args[k])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Displays a dictionary with attributes """
        listAtr = ['id', 'size', 'x', 'y']
        dictRes = {}

        for key in listAtr:
            if key == 'size':
                dictRes[key] = getattr(self, 'width')
            else:
                dictRes[key] = getattr(self, key)

        return dictRes
