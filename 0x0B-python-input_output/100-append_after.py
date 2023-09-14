#!/usr/bin/python3
"""Represents a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Adds text after each line containing a given string in a file.

    Args:
        filename (str): file's name.
        search_string (str): string to be searched for in the file.
        new_string (str):string to be inserted.
    """
    txt = ""
    with open(filename) as rr:
        for line in rr:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as ww:
        ww.write(txt)
