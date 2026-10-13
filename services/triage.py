import json
from pathlib import Path

from services.types import TicketDictType

from services.types import Priority
from services.types import Urgency

from utils.validators import require_non_empty
from utils.validators import validate_cases
from utils.validators import get_category
from utils.validators import get_urgency

from utils.helpers import generate_id

from services.exceptions import DataBaseError, InvalidTicketIDError

DATA_DIR = Path(__file__).resolve().parent.parent/'data'
FILE_PATH = DATA_DIR/"tickets.json"

class Triage:
    def __init__(self):
        self.tickets: dict[str, TicketDictType] = {}

    def create_ticket(
        self,
        title: str,
        category: str,
        urgency: str,
        cases: str
    ) -> str:

        require_non_empty(title, "Title")
        validated_category = get_category(category)
        validated_urgency = get_urgency(urgency)
        validated_cases = validate_cases(cases)

        ticket_id = generate_id()

        while ticket_id in self.tickets:
            print("Generating unique ticket ID...")
            ticket_id = generate_id()

        priority = self.set_priority(validated_cases, validated_urgency)

        self.tickets[ticket_id] = {
            "id": ticket_id,
            "title": title,
            "category": validated_category,
            "urgency": validated_urgency,
            "cases": validated_cases,
            "priority": priority,
            "assigned_staff": None
        }
        
        return ticket_id
    
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
            return "There are no tickets available. Please create one."
        
        ticket_list_str = (
            "\n------ Tickets List ------\n"
        )

        for idx, ticket in enumerate(self.tickets.values()):
            ticket_list_str += (
                f"{idx+1}  {ticket["id"]}  {ticket['title']}\n"
            )
        
        return ticket_list_str
    
    def view_ticket(self, ticket_id: str) -> str:
        require_non_empty(ticket_id, "Ticket ID")

        if ticket_id not in self.tickets:
            raise InvalidTicketIDError("No ticket with this ID exists.")
        
        ticket = self.tickets[ticket_id]
        
        return (
            f"ID: {ticket['id']}\n"
            f"Title: {ticket['id']}\n"
            f"Category: {ticket['category'].capitalize()}\n"
            f"Urgency: {ticket['urgency'].capitalize()}\n"
            f"Priority: {ticket['priority'].capitalize()}\n"
            f"Cases: {ticket['cases']}\n"
            f"Assigned staff: {ticket['assigned_staff']}"
        )
    
    
        
    def save(self):
        DATA_DIR.mkdir(exist_ok=True, parents=True)
        try:
            with open(FILE_PATH, 'w') as file:
                json.dump(self.tickets, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as err:
            raise DataBaseError(f"Session could not be saved: {err}")
        
    def load(self):
        try:
            with open(FILE_PATH, 'r') as file:
                raw_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as err:
            raise DataBaseError(f"Session could not be loaded: {err}")
        else:
            self.tickets = raw_data