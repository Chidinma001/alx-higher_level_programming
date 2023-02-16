#!/usr/bin/python3
"""The save to json file module."""


def save_to_json_file(my_obj, filename):
    """Inside the func.
    
    Args:
        my_obj (Any): Any obj.
        filename (str): file name.
    """
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
