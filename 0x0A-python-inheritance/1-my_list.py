#!/usr/bin/python3
"""
Represents the MyList class
"""


class MyList(list):
    """Implementation sorted printing for the built-in list class."""

    def print_sorted(self):
        """Returns a list in sorted ascending order."""
        print(sorted(self))
