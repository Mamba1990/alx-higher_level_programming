#!/usr/bin/python3
"""Represents a text file reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
