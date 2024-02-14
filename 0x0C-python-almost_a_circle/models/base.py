#!/usr/bin/python3
import json

"""Defines the Base class."""


class Base:
    """Base class used to manage id atrr"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base intance with id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representations"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON str representation of list objects"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj
                in list_objs])
            file.write(json_string)
