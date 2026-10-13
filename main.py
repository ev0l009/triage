from services.exceptions import InvalidAttributeError, InvalidTicketIDError

from services.triage import Triage

from services.ui import main_menu

from services.ui import categories_menu, urgency_menu

triage = Triage()

def triange_runner():
    try:
        triage.load()
    except:
        raise

    opt = "0"

    while opt != "7":
        
        if opt == "0":
            opt = input(main_menu)

        elif opt == "1":

            title = input("Ticket title: ")
            category = input(categories_menu)
            urgency = input(urgency_menu)
            cases = input("Number of cases: ")

            try:
                ticket_id = triage.create_ticket(
                    title, 
                    category, 
                    urgency, 
                    cases
                )
            except InvalidAttributeError as err:
                print(err)
            else:
                print(f"Ticket with ID: {ticket_id} successfully created.")

            opt = "0"

        elif opt == "2":
            print(triage.list_tickets())

            opt = "0"

        elif opt == "3":
            try:
                ticket_details = triage.view_ticket(
                    input("Enter a valid ticket ID: ")
                )
            except InvalidAttributeError as err:
                print(err)
            except InvalidTicketIDError as err:
                print(err)
            else:
                print(ticket_details)

            opt = "0"

        elif opt == "4":
            print("Assigning ticket...")

            opt = "0"

        elif opt == "5":
            print("Loading work queue...")

            opt = "0"

        elif opt == "6":
            print("Loading reports...")

            opt = "0"

        elif opt not in ["1","2","3","4","5","6","7"]:
            print("Invalid option. Try again...")

            opt = "0"

    try:
        triage.save()
    except:
        raise
    else:
        print("Session saved.\n")
    finally:
        print("Exiting...\n")

triange_runner()

# try:
#     triage.create_ticket(
#         "Title",
#         "1",
#         "2",
#         '1'
#     )
# except InvalidAttributeError as err:
#     print(f"Err: {err}")
# else:
#     print(triage.tickets)

# triage.load()
# print(triage.tickets)