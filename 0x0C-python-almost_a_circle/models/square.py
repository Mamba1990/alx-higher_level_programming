#!/usr/bin/python3
"""Represents a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a new Square.

        Args:
            size (int): new Square's.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The sqaure's identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getting/setting the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the Square.

        Args:
            *args (ints): New attribute values.
                - first argument is the id attribute
                - second argument is the size attribute
                - thirth argument is the x attribute
                - fourth argument is the y attribute
            **kwargs (dict): key/value pairing of attributes.
        """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ar == 1:
                    self.size = arg
                elif ar == 2:
                    self.x = arg
                elif ar == 3:
                    self.y = arg
                ar += 1

        elif kwargs and len(kwargs) != 0:
            for j, v in kwargs.items():
                if j == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif j == "size":
                    self.size = v
                elif j == "x":
                    self.x = v
                elif j == "y":
                    self.y = v

    def to_dictionary(self):
        """Displays the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns the representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
