#!/usr/bin/python3

def safe_print_division(a, b):
    """Computs the division of a by b."""
    try:
        dv = a / b
    except (TypeError, ZeroDivisionError):
        dv = None
    finally:
        print("Inside result: {}".format(dv))
    return (dv)
