from pytest import raises
from .email import parse_email

def test_validating_email():
    """
    Test the check_email method.
    """
    email = parse_email("test@mail.com")
    assert email == "test@mail.com"

    with raises(ValueError):
        parse_email("test#mail.com")
