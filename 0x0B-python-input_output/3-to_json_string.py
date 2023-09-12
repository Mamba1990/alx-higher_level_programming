#!/usr/bin/python3
"""Represents a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Displays the JSON representation of a string object."""
    return json.dumps(my_obj)
