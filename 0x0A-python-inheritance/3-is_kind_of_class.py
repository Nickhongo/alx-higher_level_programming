#!/usr/bin/python3
"""
This function:
    is_kind_of_class: True if obj is an instance of a_class or its subclass, 
    False otherwise.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns true if the obj is an instance or False if otherwise
    Args:
    obj: object
    a_class: class

    """
    return isinstance(obj, a_class)
