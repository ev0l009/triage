from enum import Enum

from services.types import Categories
from services.types import Urgency

from services.exceptions import InvalidAttributeError

def require_non_empty(value: str, field_name: str):
    if not value.strip():
        raise InvalidAttributeError(f"{field_name} cannot be empty")

def validate_cases(value: str):
    try:
        int_val = int(value)
    except ValueError:
        raise InvalidAttributeError("Number of cases must be an integer.")
    
    if int_val <= 0:
        raise InvalidAttributeError("Numbers of cases must be greater than 0.")
    return int_val

def get_category(opt: str) -> str:
    options = {
        '1': Categories.HARDWARE.value,
        '2': Categories.SOFTWARE.value,
        '3': Categories.NETWORK.value,
        '4': Categories.OTHER.value,
    }
    
    if opt not in options:
        raise InvalidAttributeError("Invalid urgency option.")
        
    return options[opt]
    
def get_urgency(opt: str) -> str:
    options = {
        '1': Urgency.LOW.value,
        '2': Urgency.MEDIUM.value,
        '3': Urgency.HIGH.value
    }
    
    if opt not in options:
        raise InvalidAttributeError("Invalid urgency option.")
        
    return options[opt]
