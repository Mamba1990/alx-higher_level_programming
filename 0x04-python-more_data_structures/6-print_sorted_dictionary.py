#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys
    """
    key = list(a_dictionary.keys())
    key.sort()
    for k in key:
        print("{}: {}".format(k, a_dictionary[k]))
