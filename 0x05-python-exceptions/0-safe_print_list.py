#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Displays x elememts of a given list.

    Args:
        my_list (list): The list to print elements from.
        x (int): number of the lists elements to print.

    Returns:
        The number of elements
    """
    c = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            c += 1
        except IndexError:
            break
    print("")
    return (c)
