from typing import Self

from services.types import Categories
from services.types import Urgency
from services.types import TicketDictType

from utils.validators import require_non_empty
from utils.validators import validate_opt
from utils.validators import validate_cases

from utils.helpers import generate_id

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
        validate_opt(category, Categories, "Category")
        validate_opt(urgency, Urgency, "Urgency")
        no_of_cases = validate_cases(cases)

        ticket_id = generate_id()

        while ticket_id in self.tickets:
            print("Generating unique ticket ID...")
            ticket_id = generate_id()

        self.tickets[ticket_id] = {
            "id": ticket_id,
            "title": title,
            "category": category,
            "urgency": urgency,
            "cases": cases,
            "priority": "high",
            "assigned_staff": None
        }
        
        return self