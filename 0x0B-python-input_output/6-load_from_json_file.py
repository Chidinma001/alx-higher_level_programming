#!/usr/bin/python3
"""Load from json file module."""


def load_from_json_file(filename):
    """Inside the func.
    
    Args:
        filename (str): filename.
    Returns:
        Python obj.
    """
    import json
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
