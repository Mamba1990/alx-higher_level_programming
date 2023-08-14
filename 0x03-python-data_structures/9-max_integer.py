#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        _max = my_list[0]
        for k in range(len(my_list)):
            if my_list[k] > _max:
                _max = my_list[k]
        return _max
