#!/usr/bin/python3
"""
is_same_class: Returns True if an object is an instance of a class
                (False otherwise)
"""
def is_same_class(obj, a_class):
    """
    Checks if object is an instance of the specifiied class

    Args:
    obj: Object to be checked
    a_class: class specified

    Returns:
    True or False
    """
    return type(obj) is a_class
