#!/usr/bin/python3
"""defining append_file function"""


def append_write(filename="", text=""):
        """appends filename with utf-8"""
            with open(filename, "a", encoding='utf-8') as file:
                        return file.write(text)
