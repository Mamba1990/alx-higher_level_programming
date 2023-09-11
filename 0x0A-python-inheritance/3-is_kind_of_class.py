#!/usr/bin/python3
"""Represnets a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checking if an objis an instance or inherited instance of a class.

    Args:
        obj (any): object to be checked.
        a_class (type): class to match the type of object to.
    Returns:
        Success - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
