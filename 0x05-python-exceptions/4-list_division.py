st_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                # Attempt to perform the division
                result = my_list_1[i] / my_list_2[i]
                result_list.append(result)
            except ZeroDivisionError:
                # Handle division by zero
                print("division by 0")
                result_list.append(0)
            except (TypeError, ValueError):
                # Handle non-integer or non-float elements
                print("wrong type")
                result_list.append(0)
            except IndexError:
                # Handle index out of range
                print("out of range")
                result_list.append(0)
    finally:
        # Finally block (optional) - executed regardless of exceptions
        print("End of division")

    return result_list
