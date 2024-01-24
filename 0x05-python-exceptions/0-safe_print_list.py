#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=" ")
            i += 1
    except IndexError:
        None  # Handle the case where the index is out of bounds

    print()  # Print a new line after the elements
    return i
