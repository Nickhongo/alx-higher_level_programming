#!/usr/bin/python3
"""
import json
"""


import json
"""
a function that  writes an object to a text file
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an object to a test file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
