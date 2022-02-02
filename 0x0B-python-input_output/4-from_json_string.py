#!/usr/bin/python3
"""
from_json_string
"""


import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object from string
    Args:
    my_string (str): string
    """
    return json.loads(my_str)
