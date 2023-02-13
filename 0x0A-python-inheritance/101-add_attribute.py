#!/usr/bin/python3
"""Inside the func modules."""


def add_attribute(obj, att, value):
    """The add attribute func.
    
    Args:
        obj (Any): check obj attr.
        att (str): attr.
        value (Any): value of attr.
    Raises:
        TypeError.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
