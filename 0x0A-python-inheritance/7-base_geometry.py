#!/usr/bin/python3

"""
BaseGeometry: empty class
"""


class BaseGeometry:

    """
    BaseGeometry defined
    """
    def area(self):

        """Raises an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
