from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from app.iam.email import parse_email
from app.iam.password import compare_password, hash_password

@dataclass
class User:
    """
    User is a class that represents the authenticated user
    """
    username: str = field(compare=False)
    bio: str | None = field(default=None, compare=False)
    # NOTE this should not be `none`
    credentials: Credentials | None = field(default=None, compare=False)
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        if len(self.username) < 3 or len(self.username) > 20:
            raise ValueError("username must be between 3 and 20 characters")
        if self.bio is not None and len(self.bio) > 100:
            raise ValueError("bio must be less than 100 characters")

@dataclass(frozen=True)
class Credentials:
    """
    Credential is a class that represents the user's login details
    """
    email: str
    password: bytes

    def compare_password(self, password: str) -> bool:
        """
        Compare a password with a hashed password. An exception will be
        raised if the passwords do not match.
        """
        return compare_password(password, self.password)
    
    def parse_credential(email: str, password: str) -> Credentials:
        return Credentials(email=email)

def parse_credentials(email: str, password: str) -> Credentials:
    """
    Parse untrusted data into a Credentials object.
    """
    hash = hash_password(password)  # hash the password
    email = parse_email(email)  # validate the email

    return Credentials(email, hash)