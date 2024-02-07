#!/usr/bin/python3
"""
import json
"""


import json
"""
a function that  creates an object from a JSON file
"""


def load_from_json_file(filename):
    """
    a function that creates an object to a JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)
