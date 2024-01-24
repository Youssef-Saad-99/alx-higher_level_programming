afe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=" ")
            printed_elements += 1
    except IndexError:
        pass  # Handle the case where the index is out of bounds

    print()  # Print a new line after the elements
    return printed_elements
