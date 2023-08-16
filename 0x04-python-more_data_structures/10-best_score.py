#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    """
    if a_dictionary:
        myList = list(a_dictionary.keys())
        _score = 0
        _leader = ""
        for k in myList:
            if a_dictionary[k] > _score:
                _score = a_dictionary[k]
                _leader = k
        return _leader
