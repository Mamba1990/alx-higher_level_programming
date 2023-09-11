#!/usr/bin/python3
"""
Represents the MyList class
"""


class MyList(list):
    """The subclass of list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """returns the sorted list"""
        print(sorted(self))
