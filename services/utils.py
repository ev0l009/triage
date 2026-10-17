"""Handles ticket id generation, menus and validation"""

# required for randomly generating ids
import string
import secrets

# valid categories and urgency values
from services.types import Categories, Urgency


def generate_id() -> str:
    """Generates a random id with a constant preffix
    
    Returns:
        - `str` - random id with constant preffix"""
    character_pool = string.ascii_letters + string.digits
    preffix = "tkt"
    suffix = "".join(secrets.choice(character_pool) for _ in range(5))
    return f"{preffix}-{suffix}"

def get_main_menu_opt() -> str:
    """Displays the main menu, validates user input and redirects to the next point in the app.
    
    Return
        - `str` - next state in the app"""
    options: dict[str, str] = {
        "1": "create_ticket",
        "2": "view_ticket",
        "3": "list_tickets",
        "4": "assign_ticket",
        "5": "work_queue",
        "6": "reports",
        "7": "exit"
    }

    choice = input(
        "========= TRIAGE ==========\n"
        "1. Create ticket\n"
        "2. View ticket\n"
        "3. List tickets\n"
        "4. Assign ticket\n"
        "5. Work queue\n"
        "6. Reports \n"
        "7. Exit\n"
        "_____________________________\n"
        "Select an option(1-7): "
    )

    if choice not in options:
        print("\nInvalid selection. Try again\n")
        return "main_menu"
    
    return options[choice]

def require_non_empty(value: str, field_name: str):
    """Checks that a value is not empty and returns a stripped value.
    
    Args
        - value `str` - value to be checked
        - field_name `str` - name of field for error messsage."""
    if not value.strip():
        print(f"\n{field_name} cannot be empty. Try again\n")
        return
    
    return value.strip()

def get_category() -> str | None:
    """Displays the categories menu and validates user input.
    
    Returns
        - `str` - selected category
        - `None` - early return when an invalid option is entered."""
    options: dict[str, str] = {
        "1": Categories.HARDWARE.value,
        "2": Categories.SOFTWARE.value,
        "3": Categories.NETWORK.value,
        "4": Categories.OTHER.value
    }

    choice: str = input(
        "\n----- Select a category -----\n"
        "1. Hardware\n"
        "2. Software\n"
        "3. Network\n"
        "4. Other"
        "_____________________________\n"
        "Select an option: "
    )

    if choice not in options:
        print("\nInvalid Category option. Try again\n")
        return
    
    return options[choice]

def get_urgency() -> str | None:
    """Displays the urgency menu and validates user input.
    
    Returns
        - `str` - selected urgency
        - `None` - early return when an invalid option is entered."""
    options: dict[str, str] = {
        "1": Urgency.HIGH.value,
        "2": Urgency.MEDIUM.value,
        "3": Urgency.LOW.value,
    }

    choice: str = input(
        "\n----- Select an urgency level -----\n"
        "1. High\n"
        "2. Medium\n"
        "3. Low\n"
        "___________________________________\n"
        "Select an option: "
    )

    if choice not in options:
        print("\nInvalid Urgency option. Try again\n")
        return
    
    return options[choice]

def get_validate_cases() -> int | None:
    """Validates user input for number of cases.
    
    Returns
        - `int` - number of cases
        - `None` - early return when an invalid case value is entered."""

    cases = input("Number of cases: ")

    try:
        int_val = int(cases)
    except ValueError:
        print("\nNumber of cases must be an integer. Try again\n")
        return
    
    if int_val <= 0:
        print("\nNumber of cases must be greater than zero. Try again\n")
        return
    
    return int_val