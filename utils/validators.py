from services.types import Categories, Urgency

from services.exceptions import InvalidAttributeError

from services.types import Categories, Urgency

def require_non_empty(value: str, field_name: str):
    if not value.strip():
        print(f"{field_name} cannot be empty")
        return
    
    return value.strip()

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

def get_urgency() -> str:
    options: dict[str, str] = {
        "1": Urgency.HIGH.value,
        "2": Urgency.MEDIUM.value,
        "3": Urgency.LOW.value,
    }

    choice: str = (
        "----- Select an urgency level -----\n"
        "1. High\n"
        "2. Medium\n"
        "3. Low\n"
        "___________________________________\n"
        "Select an option: "
    )

    if choice not in options:
        print("Invalid Urgency option.")
        return
    
    return options[choice]

def get_validate_cases() -> int:

    cases = input("Number of cases: ")

    try:
        int_val = int(cases)
    except ValueError:
        print("Number of cases must be an integer.")
        return
    
    if int_val <= 0:
        print("Number of cases must be greater than zero.")
        return
    
    return int_val