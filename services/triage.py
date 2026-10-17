import json
from pathlib import Path

from services.types import TicketDictType

from services.types import Priority, Urgency, TicketStatus

from services.utils import require_non_empty
from services.utils import get_validate_cases
from services.utils import get_category
from services.utils import get_urgency

from services.utils import generate_id

from services.exceptions import DataBaseError, InvalidTicketIDError

DATA_DIR = Path(__file__).resolve().parent.parent/'data'
FILE_PATH = DATA_DIR/"tickets.json"

PRIORITY_SORT_ORDER: dict[str, int] = {
    Priority.CRITICAL.value: 1,
    Priority.HIGH.value: 2,
    Priority.MEDIUM.value: 3,
    Priority.LOW.value: 4
}

class Triage:
    
    def __init__(self):
        self.tickets: dict[str, TicketDictType] = {}

    def create_ticket(self) -> str:
        
        title = input("\nTicket title: ")

        validated_title = require_non_empty(title, "Title")
        if validated_title is None:
            return
        
        validated_category = get_category()
        if validated_category is None:
            return
        
        validated_urgency = get_urgency()
        if validated_urgency is None:
            return
        
        validated_cases = get_validate_cases()
        if validated_cases is None:
            return

        ticket_id = generate_id()

        while ticket_id in self.tickets:
            print("\nGenerating your unique ticket ID....\n")
            ticket_id = generate_id()

        priority = self.set_priority(validated_cases, validated_urgency)

        self.tickets[ticket_id] = {
            "id": ticket_id,
            "title": title,
            "category": validated_category,
            "urgency": validated_urgency,
            "cases": validated_cases,
            "priority": priority,
            "status": TicketStatus.OPEN.value,
            "assigned_staff": "None"
        }

        print(
            "Ticket creation successful.\n"
            f"Ticket ID: {ticket_id}\n"
        )
        
        return self.tickets
    
    def set_priority(self, cases: int, urgency: str) -> str:
        if urgency == Urgency.HIGH.value and cases >= 10:
            return Priority.CRITICAL.value
        elif urgency == Urgency.HIGH.value or cases >= 10:
            return Priority.HIGH.value
        elif urgency == Urgency.MEDIUM.value or cases >= 3:
            return Priority.MEDIUM.value
        else:
            return Priority.LOW.value
        
    def list_tickets(self) -> str:

        if not self.tickets:
            return "\nThere are no tickets available. Please create one.\n"
        
        ticket_list_str = (
            "\n------ Tickets List ------\n"
        )

        for idx, ticket in enumerate(self.tickets.values()):
            ticket_list_str += (
                f"{idx+1}  {ticket["id"]}  {ticket['title']} {ticket['status'].capitalize()}\n"
            )
        
        print(ticket_list_str)
    
    def view_ticket(self) -> str:
        ticket_id = input("\nEnter Ticket ID: ")

        ticket_id = require_non_empty(ticket_id, "Ticket ID")
        if not ticket_id:
            return

        if ticket_id not in self.tickets:
            print("\nNo ticket with this ID exists. Try again.\n")
            return
        
        ticket = self.tickets[ticket_id]
        
        print(
            f"ID: {ticket['id']}\n"
            f"Title: {ticket['id']}\n"
            f"Category: {ticket['category'].capitalize()}\n"
            f"Urgency: {ticket['urgency'].capitalize()}\n"
            f"Priority: {ticket['priority'].capitalize()}\n"
            f"Cases: {ticket['cases']}\n"
            f"Assigned staff: {ticket['assigned_staff']}\n"
            f"Status: {ticket['status']}"
        )

    def assign_ticket(self):
        ticket_id = input(f"\nEnter a valid Ticket ID: ")

        ticket_id = require_non_empty(ticket_id, "Ticket ID")
        if not ticket_id:
            return

        if ticket_id not in self.tickets:
            print("\nNo ticket with this ID exists.\n")
            return
        
        staff_name = require_non_empty(
            input("Enter staff name:"), 
            "Staff Name"
        )

        if not staff_name:
            return

        ticket = self.tickets[ticket_id]

        ticket["assigned_staff"] = staff_name
        self.set_ticket_status(ticket)

        return f"Ticket with ID {ticket_id} successfully assigned to {staff_name}."
    
    def set_tickets_status(self):
        for ticket in self.tickets.values():
            self.set_ticket_status(ticket)
    
    def set_ticket_status(self, ticket: TicketDictType):

        if not ticket["assigned_staff"].strip():
            ticket["status"] = TicketStatus.OPEN.value
        elif ticket["assigned_staff"]:
            ticket["status"] = TicketStatus.IN_PROGRESS.value
        else:
            ticket["status"] = TicketStatus.RESOLVED.value

    def show_work_queue(self) -> str:

        if not self.tickets:
            print("\nThere are no tickets available. Please create one.\n")
            return

        ticket_list: list[TicketDictType] = list(self.tickets.values())

        ticket_list.sort(
            key=lambda ticket: PRIORITY_SORT_ORDER.get(ticket["priority"], 99)
        )

        sorted_ticket_list = (
            "\n------ Work Queue ------\n"
        )

        for idx, ticket in enumerate(self.tickets.values()):
            sorted_ticket_list += (
                f"{idx+1}  {ticket["id"]}  {ticket['title']} {ticket['priority'].capitalize()}\n"
            )

        print(sorted_ticket_list)
    
    def show_report(self) -> str:

        report = (
            "\n------ Report ------\n"
            "No of tickets: \n"
            "No of open tickets: \n"
            "No of assigned tickets: \n"
            "No of resolved tickets: \n"
        )

        print(report)

    def save(self):

        try:
            with open(FILE_PATH, 'w') as file:
                json.dump(self.tickets, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as err:
            print(f"\nCouldn't save session.")
        else:
            print(f"\nYour session has been saved.\n")
        
    def load(self):

        DATA_DIR.mkdir(exist_ok=True, parents=True)

        try:
            with open(FILE_PATH, 'r') as file:
                raw_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as err:
            print(f"\nSession could not be loaded\n")
            self.tickets = {}
        else:
            self.tickets = raw_data
            print("\nTriage loading successful.\n")