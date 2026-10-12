from typing import Type
from enum import Enum

from services.exceptions import InvalidAttributeError

def require_non_empty(value: str, field_name: str):
    if not value.strip():
        raise InvalidAttributeError(f"{field_name} cannot be empty")

def validate_opt(
    value: str, 
    valid_options: Enum, 
    field_name: str
):
    if value not in valid_options._value2member_map_:
        raise InvalidAttributeError(f"{value} is not a valid {field_name} option.")

def validate_cases(value: str):
    try:
        int(value)
    except ValueError:
        raise InvalidAttributeError("Number of cases must be an integer.")
    
    if int(value) <= 0:
        raise InvalidAttributeError("Numbers of cases must be greater than 0.")