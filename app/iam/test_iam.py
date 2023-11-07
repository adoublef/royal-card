from pytest import fixture
from uuid import uuid4
from ..iam import User, Credentials, parse_credentials

@fixture
def valid_credentials():
    email, password = ("test@mail.com", "this is a valid password")
    return parse_credentials(email=email, password=password)

def test_user_equality(valid_credentials: Credentials):
    user1 = User(id=uuid4(), username="foo")
    user2 = User(id=user1.id, username="bar", credentials=valid_credentials)
    assert user1 == user2
    assert user1 is not user2