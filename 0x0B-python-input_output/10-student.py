#!/usr/bin/python3
"""
defines class
"""


class Student:
    """
    Defines a class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = ["first_name", "last_name", "age"]

        if not isinstance(attrs, list):
            raise TypeError("attrs must be a list of strings")

        result = {}
        for attr in attrs:
            if not isinstance(attr, str):
                raise TypeError("attrs must contain only strings")
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
