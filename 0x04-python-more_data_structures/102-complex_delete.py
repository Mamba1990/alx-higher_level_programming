#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listKeys = list(a_dictionary.keys())

    for v_dic in listKeys:
        if value == a_dictionary.get(v_dic):
            del a_dictionary[v_dic]

    return (a_dictionary)
