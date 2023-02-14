#!/usr/bin/python3
"""The inherit_from module."""


def inherits_from(obj, a_class):
    """Inside the inherits_from.
    
    Args:
        obj (Any): Check this obj.
        a_class (type): is of this type.
    Returns:
        Boolean.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
