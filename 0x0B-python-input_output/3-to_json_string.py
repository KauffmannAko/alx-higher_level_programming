#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """_serialize an object_

    Args:
        my_obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    return json.dumps(my_obj)