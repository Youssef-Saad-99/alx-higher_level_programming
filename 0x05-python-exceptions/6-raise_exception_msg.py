se_exception_msg(message=""):
    try:
        # Attempt to raise a name exception
        raise NameError(message)
    except NameError as e:
        # Handle the name exception and print the specified message
        print("Name Exception:", e)
