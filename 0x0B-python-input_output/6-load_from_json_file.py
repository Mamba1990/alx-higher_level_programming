#!/usr/bin/python3
"""Represents a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creating a Python object from a JSON file."""
    with open(filename) as fi:
        return json.load(fi)
