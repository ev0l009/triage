from services.ui import get_main_menu_opt

from services.triage import Triage

def triage_runner():
    current_state = "main_menu"

    triage = Triage()

    print("\nLoading tickets\n")

    while current_state != "exit":

        if current_state == "main_menu":
            current_state = get_main_menu_opt()

        elif current_state == "create_ticket":
            triage.create_ticket()
            current_state = "main_menu"

        elif current_state == "view_ticket":
            print("\nOpening ticket\n")
            current_state = "main_menu"

        elif current_state == "list_tickets":
            print("\nDisplaying all tickets\n")
            current_state = "main_menu"

        elif current_state == "assign_ticket":
            print("\nAssigning ticket\n")
            current_state = "main_menu"

        elif current_state == "work_queue":
            print("\nDisplaying work queue\n")
            current_state = "main_menu"

        elif current_state == "reports":
            print("\nDisplaying reports\n")
            current_state = "main_menu"

        else:
            print("\nInvalid selection. Try again\n")
    
    print("\nSaving tickets\n")

    print("\nExiting\n")

triage_runner()