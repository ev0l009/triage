"""Holds valid options values and types for type hinting."""
from enum import Enum
from typing import TypedDict

class Categories(Enum):
    """Valid category options"""
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    NETWORK = "Network"
    OTHER = "Other"

class Urgency(Enum):
    """Valid urgency options"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Priority(Enum):
    """Valid priority values."""
    CRITICAL = 'critical'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

class TicketDictType(TypedDict):
    """Describes the ticket dictionay"""
    id: str
    title: str
    category: str
    urgency: str
    cases: int
    priority: str
    status: str
    assigned_staff: str

class TicketStatus(Enum):
    """Valid ticket status"""
    OPEN = "open"
    IN_PROGRESS = "in progress"
    RESOLVED = "resolved"