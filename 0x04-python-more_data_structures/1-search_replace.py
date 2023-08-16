#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces occurrences
    of an element by another in a new list
    """
    newList = []
    for e in my_list:
        if e == search:
            newList.append(replace)
        else:
            newList.append(e)
    return newList
