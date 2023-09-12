#!/usr/bin/python3
"""Represents a class Student."""


class Student:
    """Degines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): student's first name.
            last_name (str): student's last name..
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student."""
        return self.__dict__
