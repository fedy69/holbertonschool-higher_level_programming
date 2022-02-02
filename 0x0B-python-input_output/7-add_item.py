#!/usr/bin/python3
"""
add_item function
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    text = load_from_json_file(filename)
except FileNotFoundError:
    text = []

save_to_json_file(text + argv[1:], filename)
