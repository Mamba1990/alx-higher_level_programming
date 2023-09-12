#!/usr/bin/python3
"""Represents a file-appending function."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (str): file's name to append to.
        text (str): string to be appended to the file.
    Returns:
        The number of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as fi:
        return fi.write(text)
