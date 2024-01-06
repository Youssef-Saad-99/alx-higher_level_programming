#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = [i for i in range(len(my_list))]
    if idx > len(my_list):
        return my_list
    elif idx < 0:
        return my_list
    else:
        newlist = []
        newlist = copy
        for i in range(len(copy)):
            if i == idx:
                newlist[i] = element
        return newlist
