import string
import secrets

def generate_id() -> str:
    character_pool = string.ascii_letters + string.digits
    preffix = "tkt"
    suffix = "".join(secrets.choice(character_pool) for _ in range(5))
    return f"{preffix}-{suffix}"

def get_main_menu_opt() -> str:
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