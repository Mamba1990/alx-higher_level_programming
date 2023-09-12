#!/usr/bin/python3
"""Represents a file-writing function."""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str): file's name to be writen.
        text (str): text to be writen to the file.
    Returns:
        number of chars written.
    """
    with open(filename, "w", encoding="utf-8") as fi:
        return fi.write(text)
