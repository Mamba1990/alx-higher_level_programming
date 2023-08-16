#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique
    integers in a list
    """
    newList = []
    _sum = 0
    for number in my_list:
        if number not in newList:
            _sum += number
            newList.append(number)
    return _sum
