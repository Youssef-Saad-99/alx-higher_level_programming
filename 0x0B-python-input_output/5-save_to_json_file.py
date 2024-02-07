#!/usr/bin/python3
"""defining save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
        """writes filename with utf-8"""
        with open(filename, "w", encoding='utf-8') as file:
                json.dump(my_obj, file)
