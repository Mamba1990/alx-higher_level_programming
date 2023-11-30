#!/usr/bin/python3
"""Finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: integers' list

    Returns:
        int: peak(s)
    """
    _list = list_of_integers
    if _list == []:
        return None
    leng = len(_list)

    start, end = 0, leng - 1
    while start < end:
        mid = start + (end - start) // 2
        if _list[mid] > _list[mid - 1] and _list[mid] > _list[mid + 1]:
            return _list[mid]
        if _list[mid - 1] > _list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return _list[start]
