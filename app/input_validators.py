# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

from .exceptions import ValidationError

def parse_two_numbers(parts):
    # LBYL: ensure enough parts
    if len(parts) != 3:
        raise ValidationError("Expected two numbers, e.g. 'add 1 2'")
    try:  # EAFP parse
        a = float(parts[1])
        b = float(parts[2])
    except ValueError as e:
        raise ValidationError("Arguments must be numbers") from e
    return a, b
