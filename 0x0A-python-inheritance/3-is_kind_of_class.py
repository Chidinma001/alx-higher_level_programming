#!/usr/bin/python3
"""The is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """Inside the is_kind_of_class func.
    
    Args:
        obj (Any): check object is an instance of a class.
        a_class (type): the type.
    Returns:
        Boolean.
    """
    if isinstance(obj, a_class):
        return True
    return False
