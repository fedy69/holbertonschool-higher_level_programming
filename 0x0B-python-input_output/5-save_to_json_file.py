#!/usr/bin/python3
"""
save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON respresentation
    Args:
    my_obj (str): object to write to a text file
    filename (str): file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
