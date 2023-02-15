#!/usr/bin/python3
"""Class to json module."""


def class_to_json(obj):
    """Inside the func.
    
    Args:
        obj (Any): obj.
    """
    return obj.__dict__
