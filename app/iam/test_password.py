from pytest import raises

from .password import password_entropy, hash_password, compare_password

def test_password_entropy():
    """
    Test the entropy of a password.
    """
    entropy = password_entropy("this is a password")
    assert entropy > 0.66


def test_hash_password():
    """
    Test the hash_password method.
    """

    hashed_password = hash_password("this is a password")
    assert hashed_password is not None

    ok = compare_password("this is a password", hashed_password)
    assert ok is True


def test_hash_password_mismatch():
    """
    Test the hash_password method.
    """

    hashed = hash_password("this is a password")
    assert hashed is not None

    with raises(ValueError):
        compare_password("this is not a password", hashed)