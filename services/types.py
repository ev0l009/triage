from enum import Enum
from typing import TypedDict

class Categories(Enum):
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    NETWORK = "Network"
    OTHER = "Other"

class Urgency(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Priority(Enum):
    CRITICAL = 'critical'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

class TicketDictType(TypedDict):
    id: str
    title: str
    category: str
    urgency: str
    cases: int
    priority: str
    status: str
    assigned_staff: str

class TicketStatus(Enum):
    OPEN = "open"
    IN_PROGRESS = "in progress"
    RESOLVED = "resolved"