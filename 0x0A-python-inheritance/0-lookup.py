#!/usr/bin/python3
"""The module docstring."""

def lookup(obj):
    """The lookup function.
    
    Args:
        obj: object to look up class attributes and methods.
    Return:
        list
    """
    return dir(obj)
