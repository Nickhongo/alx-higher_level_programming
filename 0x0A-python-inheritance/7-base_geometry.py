#!/usr/bin/python3

"""
BaseGeometry: empty class
"""


class BaseGeometry:

    """
    BaseGeometry class representation
    """
    def area(self):

        """Raises an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value given asa an integer

        Args:
        name: a str representing name
        value: value to be validated

        Raises:
        TypeError: if value is not integer
        ValueError: if value is <= 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
