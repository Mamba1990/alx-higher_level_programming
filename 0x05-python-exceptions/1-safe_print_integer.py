#!/usr/bin/python3

def safe_print_integer(value):
    """Printsan integer with "{:d}".format().

    Args:
        value (int): integer to be printed.

    Returns:
        False - TypeError or ValueError.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
