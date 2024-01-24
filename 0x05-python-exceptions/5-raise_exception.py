se_exception():
    try:
        # Attempt to perform an operation that raises a type exception
        result = "string" + 42
    except TypeError as e:
        # Handle the type exception
        print("Type Exception:", e)
