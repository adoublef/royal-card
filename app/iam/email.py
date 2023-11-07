from email_validator import validate_email, EmailSyntaxError

def parse_email(email: str) -> bool:
    """
    Check if an email is valid. If it is, return the normalized form.
    """
    try:
        address = validate_email(email)
    except EmailSyntaxError:
        raise ValueError("Is not a valid RFC 5322 email address")
    except Exception as e:
        raise e
    return address.normalized
