from services.exceptions import InvalidAttributeError

from services.triage import Triage

triage = Triage()


try:
    triage.create_ticket(
        "Title",
        "Hardware",
        "low",
        '2'
    )
except InvalidAttributeError as err:
    print(f"Err: {err}")
else:
    print(triage.tickets)