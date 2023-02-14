#!/usr/bin/python3
"""The is_same_class module."""


def is_same_class(obj, a_class):
    """The is_same_class func.
    
    Args:
        obj (Any): check this obj.
        a_cass (type): class type.
    Returns:
        Boolean
    """
    if type(obj) == a_class:
        return True
    return False
