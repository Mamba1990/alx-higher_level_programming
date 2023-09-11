#!/usr/bin/python3
"""Reprents an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checking if an object is an inherited instance of a class.

    Args:
        obj (any):object to be checked.
        a_class (type): class to be matched to the type of obj to.
    Returns:
        Success- True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
