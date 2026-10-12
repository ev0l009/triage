from services.exceptions import InvalidAttributeError

from services.triage import Triage

triage = Triage()


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

triage.load()
print(triage.tickets)