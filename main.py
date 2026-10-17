from services.triage import Triage

from services.utils import get_main_menu_opt

def triage_runner():
    current_state = "main_menu"

    triage = Triage()

    triage.load()

    while current_state != "exit":

        if current_state == "main_menu":
            current_state = get_main_menu_opt()

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
    
    triage.save()

    print("\nExiting\n")

triage_runner()