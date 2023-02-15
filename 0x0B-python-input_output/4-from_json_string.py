#!/usr/bin/python3
"""From JSon string module."""


def from_json_string(my_str):
    """Inside the func.
    
    Args:
        my_str (json str): JSON str to deserialize.
    Returns:
       Python obj (Any)
    """
    import json
    return json.loads(my_str)
