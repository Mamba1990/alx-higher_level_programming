#!/usr/bin/python3
"""Represents a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adding a new attribute to an object if possible.

    Args:
        obj (any): object to be added an attribute to.
        att (str): name of the attribute to be added to obj.
        value (any): attribute's value.
    Raises:
        TypeError: attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
