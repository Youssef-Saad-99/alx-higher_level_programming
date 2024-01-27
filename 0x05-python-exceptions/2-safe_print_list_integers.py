#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for i in range(x):
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(value), end=" ")
                printed_integers += 1
    except (IndexError, ValueError, TypeError):
        pass  # Handle the cases where the index is out of bounds or the value is not an integer

    print()  # Print a new line after the integers
    return printed_integers
