#!/usr/bin/python3
"""Represents a class-checking function."""


def is_same_class(obj, a_class):
    """ if an object is exactly an instance of a given class.

    Args:
        obj (any): object to be checked.
        a_class (type): class to match the type of obj to.
    Returns:
        success - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
