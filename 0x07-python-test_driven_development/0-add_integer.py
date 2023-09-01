#!/usr/bin/python3
"""Return the sum of two intgers."""


def add_integer(a, b=98):
    """Returning the integer addition of a and b.

    Float arguments are casted to integers firstly.

    Raises:
        TypeError: If a or b is not an integer or not a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
