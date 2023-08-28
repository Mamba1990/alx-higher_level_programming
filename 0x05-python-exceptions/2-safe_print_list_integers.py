#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to be printed.

    Returns:
        number of elements printed.
    """
    c = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            c += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (c)
