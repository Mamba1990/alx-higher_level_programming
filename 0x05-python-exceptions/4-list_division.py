#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divids to elements"""
    newList = []
    for k in range(0, list_length):
        try:
            dv = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            dv = 0
        except ZeroDivisionError:
            print("division by 0")
            dv = 0
        except IndexError:
            print("out of range")
            dv = 0
        finally:
            newList.append(dv)
    return (newList)
