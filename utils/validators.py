from enum import Enum

from services.types import Categories
from services.types import Urgency

from services.exceptions import InvalidAttributeError

def require_non_empty(value: str, field_name: str):
    if not value.strip():
        raise InvalidAttributeError(f"{field_name} cannot be empty")

def validate_cases(value: str):
    try:
        int(value)
    except ValueError:
        raise InvalidAttributeError("Number of cases must be an integer.")
    
    if int(value) <= 0:
        raise InvalidAttributeError("Numbers of cases must be greater than 0.")

def get_category(opt: str) -> str:
    if opt == '1':
        return Categories.HARDWARE.value
    elif opt == '2':
        return Categories.SOFTWARE.value
    elif opt == '3':
        return Categories.NETWORK.value
    elif opt == '4':
        return Categories.OTHER.value
    else:
        raise InvalidAttributeError("Invalid category option.")
    
def get_urgency(opt: str) -> str:
    if opt == '1':
        return Urgency.LOW.value
    elif opt == '2':
        return Urgency.MEDIUM.value
    elif opt == '3':
        return Urgency.HIGH.value
    else:
        raise InvalidAttributeError("Invalid urgency option.")