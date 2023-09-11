#!/usr/bin/python3
"""Represents a base geometry class BaseGeometry."""


class BaseGeometry:
    """Defines base geometry."""

    def area(self):
        """No implementation yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """approves a parameter as an integer.

        Args:
            name (str): parameter's name
            value (int): parameter to be  validated.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
