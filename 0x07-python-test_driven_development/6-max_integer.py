#!/usr/bin/python3
"""a Module for finding the max integer in a list
"""


def max_integer(list=[]):
    """Finds and Returns the max integer in a list of integers
        and returns none if the list is empty
    """
    if len(list) == 0:
        return None
    res = list[0]
    k = 1
    while k < len(list):
        if list[k] > res:
            res = list[k]
        k += 1
    return res
