def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return("ZeroDivision Error")
    except NameError:
        return("Name Error")


print(divide(1, 0))
