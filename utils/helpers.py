import string
import secrets

def generate_id() -> str:
    character_pool = string.ascii_letters + string.digits
    preffix = "tkt"
    suffix = "".join(secrets.choice(character_pool) for _ in range(5))
    return f"{preffix}-{suffix}"
