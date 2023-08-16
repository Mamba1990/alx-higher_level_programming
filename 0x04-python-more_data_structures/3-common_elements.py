#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Func returning a set of
    common elements in two sets
    """
    commonSet = set()
    for e in set_1:
        if e in set_2:
            commonSet.add(e)
    return commonSet
