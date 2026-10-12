from typing import Self

from services.types import TicketDictType

from services.types import Priority
from services.types import Urgency

from utils.validators import require_non_empty
from utils.validators import validate_cases
from utils.validators import get_category
from utils.validators import get_urgency

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
        validate_cases(cases)
        validated_category = get_category(category)
        validated_urgency = get_urgency(urgency)

        ticket_id = generate_id()

        while ticket_id in self.tickets:
            print("Generating unique ticket ID...")
            ticket_id = generate_id()

        priority = self.set_priority(cases, validated_urgency)

        self.tickets[ticket_id] = {
            "id": ticket_id,
            "title": title,
            "category": validated_category,
            "urgency": validated_urgency,
            "cases": cases,
            "priority": priority,
            "assigned_staff": None
        }
        
        return ticket_id
    
    def set_priority(cases: int, urgency: str) -> str:
        if urgency == Urgency.HIGH.value and cases >= 10:
            return Priority.CRITICAL.value
        elif urgency == Urgency.HIGH.value or cases >= 10:
            return Priority.HIGH.value
        elif urgency == Urgency.MEDIUM.value or cases >= 3:
            return Priority.MEDIUM.value
        else:
            return Priority.LOW.value