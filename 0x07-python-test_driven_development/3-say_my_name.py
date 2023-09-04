#!/usr/bin/python3
"""Represents a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """Dispalys a name.

    Args:
        first_name (str): The 1st name to be printed .
        last_name (str): The last name to be printd.
    Raises:
        TypeError: If none of first_name or last_name are  strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
