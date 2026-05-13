import uuid


def generate_user_code() -> str:
    return uuid.uuid4().hex[:6].upper()
