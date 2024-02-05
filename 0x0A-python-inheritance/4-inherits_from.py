#!/usr/bin/python3
"""
This function:
    inherits_from: True if obj is an instance of a_class or its subclass, 
    False otherwise.
"""

def inherits_from(obj, a_class):
    """
    Returns true if the obj is an instance or False if otherwise
    Args:
    obj: object
    a_class: class

    """
    if isinstance(obj, a_class):
        return True
    for base_class in obj.__class__.__bases__:
        if inherits_from(obj, base_class):
            return True
    return False
