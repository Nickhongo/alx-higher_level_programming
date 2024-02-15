#!/usr/bin/python3

import json

"""Base class"""


class Base:
    """Base class representation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize Base Instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return Json string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)
