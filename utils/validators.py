from services.types import Categories, Urgency

from services.exceptions import InvalidAttributeError

from services.types import Categories, Urgency

def require_non_empty(value: str, field_name: str):
    if not value.strip():
        print(f"{field_name} cannot be empty")
        return
    
def get_category(opt: str) -> str:

    options: dict[str, str] = {
        "1": Categories.HARDWARE.value,
        "2": Categories.SOFTWARE.value,
        "3": Categories.NETWORK.value,
        "4": Categories.OTHER.value
    }

    if opt not in options:
        print("Invalid Category option.")
        return
    
    return options[opt]

def get_urgency(opt: str) -> str:

    options: dict[str, str] = {
        "1": Urgency.HIGH.value,
        "2": Urgency.MEDIUM.value,
        "3": Urgency.LOW.value,
    }

    if opt not in options:
        print("Invalid Urgency option.")
        return
    
    return options[opt]

def validate_cases(value: str) -> int:
    try:
        int_val = int(value)
    except ValueError:
        print("Number of cases must be an integer.")
        return
    
    if int_val <= 0:
        print("Number of cases must be greater then zero.")
        return
    
    return int_val