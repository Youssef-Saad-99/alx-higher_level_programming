#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = [i for i in range(len(my_list))]
    if idx > len(my_list):
        return my_list
    elif idx < 0:
        return my_list
    else:
        copied_list = my_list.copy()
        copied_list[idx] = element
        return copied_list
