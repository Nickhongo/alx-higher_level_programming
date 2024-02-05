#!/usr/bin/python3
def is_same_class(obj, Cclass):
    """
    Checks if object is an instance of the specifiied class

    Args:
    obj: Object to be checked
    Cclass: class specified

    Returns:
    True or False
    """
    return type(obj) is Cclass
