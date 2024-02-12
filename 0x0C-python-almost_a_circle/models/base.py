#!/usr/bin/python3
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
