#!/usr/bin/python3
"""
Defines a class
"""
def class_to_json(obj):
    """converts all instance attr in __dict__ to json
    """

    return obj.__dict__
