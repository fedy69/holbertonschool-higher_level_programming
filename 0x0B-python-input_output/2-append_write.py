#!/usr/bin/python3
"""
append_file
"""


def append_write(filename="", text=""):
    """
    function that writes a string to a text file
    Args:
    filename (str): Filename
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
