from services.auth_service import (
    password_hashing,
    verify_password,
    create_access_token,
    decode_token,
)


def test_password_hashing():
    password = "Jazz@123"
    hashed_password = password_hashing(password)
    assert password != hashed_password
    assert verify_password(
        password,
        hashed_password
    ) is True


def test_access_token():
    payload = {
        "sub": "jazz-user-id"
    }
    token = create_access_token(payload)
    decoded_payload = decode_token(token)
    assert decoded_payload is not None

    assert decoded_payload["sub"] == "jazz-user-id"