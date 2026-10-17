"""Application entry point"""

from services.triage import Triage

from services.utils import get_main_menu_opt

def triage_runner():
    """Runs the triage app and controls app flow."""

    # To store state that determines where a user can be at anypoint in the app. 
    # Resets to `main_menu after every other operation except exit.`
    current_state = "main_menu"

    triage = Triage()

    # To load previous session if any
    triage.load()

    # To maintain app flowloop until exit
    while current_state != "exit":

        if current_state == "main_menu":
            current_state = get_main_menu_opt() # shows the main menu and updates the current state

        elif current_state == "create_ticket":
            triage.create_ticket()
            current_state = "main_menu"

        elif current_state == "view_ticket":
            triage.view_ticket()
            current_state = "main_menu"

        elif current_state == "list_tickets":
            triage.list_tickets()
            current_state = "main_menu"

        elif current_state == "assign_ticket":
            triage.assign_ticket()
            current_state = "main_menu"

        elif current_state == "work_queue":
            triage.show_work_queue()
            current_state = "main_menu"

        elif current_state == "reports":
            triage.show_report()
            current_state = "main_menu"

        else:
            print("\nInvalid selection. Try again\n")
    
    # To save session on exit.
    triage.save()

    print("\nExiting\n")

triage_runner()