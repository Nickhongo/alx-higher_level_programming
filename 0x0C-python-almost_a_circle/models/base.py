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
        if isinstance(list_dictionaries, (list,)) or list_dictionaries is None:
            if type(list_dictionaries) is list:
                for _ in list_dictionaries:
                    if not isinstance(_, dict):
                        raise TypeError(
                            "list_dictionaries must be a list of dictionaries"
                        )
        else:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list represented by json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON str representation"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            json_string = cls.to_json_string(
                    [obj.to_dictionary()for obj in list_objs])
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise TypeError("create method is not defined for this class")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
