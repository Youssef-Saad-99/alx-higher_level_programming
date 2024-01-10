#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_d = {x for x in a_dictionary if x not in {key}}
    return new_d
