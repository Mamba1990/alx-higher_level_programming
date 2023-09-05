#!/usr/bin/python3
"""Represents a locked class."""


class LockedClass:
    """
    Class that Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
