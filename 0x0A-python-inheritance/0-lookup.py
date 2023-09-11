#!/usr/bin/python3
"""Represent an object attribute lookup function."""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return (dir(obj))
