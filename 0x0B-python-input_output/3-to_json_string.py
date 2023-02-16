#!/usr/bin/python3
"""Inside to_json_string module."""


def to_json_string(my_obj):
    """Inside the func.
    
    Args:
        my_obj (Any): object.
    Returns:
        json string.
    """
    import json

    return json.dumps(my_obj)
