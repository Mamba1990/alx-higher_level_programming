#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return "None"
    else:
        for i in range(0, len(my_list) - 1):
            if my_list[i] < my_list[i+1]:
                return my_list[i+1]
            else:
                return my_list[i]
