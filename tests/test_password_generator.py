import string
from password_generator import generate_password

def test_password_lower_and_digit() -> None:
    """ Tests if password returned contains at least one lowercase character and one digit. """
    password = generate_password((string.ascii_lowercase + string.digits), 15)

    assert (any(c.islower() for c in password)
        and any(c.isdigit() for c in password))

def test_password_lower_and_symbol() -> None:
    """ Tests if password returned contains at least one lowercase character and one symbol. """
    password = generate_password((string.ascii_lowercase + string.punctuation), 15)

    assert (any(c.islower() for c in password)
        and any(string.punctuation for c in password))
    
def test_password_upper_and_symbol() -> None:
    """ Tests if password returned contains at least one uppercase character and one symbol. """
    password = generate_password((string.ascii_uppercase + string.punctuation), 15)

    assert (any(c.isupper() for c in password)
        and any(string.punctuation for c in password))
    
def test_password_upper_and_digit() -> None:
    """ Tests if password returned contains at least one uppercase character and one digit. """
    password = generate_password((string.ascii_uppercase + string.digits), 15)

    assert (any(c.isupper() for c in password)
        and any(c.isdigit() for c in password))

def test_password_digit_and_symbol() -> None:
    """ Tests if password returned contains at least one digit and one symbol. """
    password = generate_password((string.digits + string.punctuation), 15)

    assert (any(c.isdigit() for c in password)
        and any(string.punctuation for c in password))
    
def test_password_lower_and_upper() -> None:
    """ Tests if password returned contains at least one lowercase and one uppercase character. """
    password = generate_password((string.ascii_lowercase + string.ascii_uppercase), 15)

    assert (any(c.islower() for c in password)
        and any(c.isupper for c in password))
    
def test_password_lower_upper_digit() -> None:
    """ Tests if password returned contains at least one lowercase, one uppercase, and one digit. """
    password = generate_password((string.ascii_lowercase + string.ascii_uppercase + string.digits), 15)

    assert (any(c.islower() for c in password)
        and any(c.isupper for c in password)
        and any(c.isdigit for c in password))
    
def test_password_lower_upper_symbol() -> None:
    """ Tests if password returned contains at least one lowercase, one uppercase, and one symbol. """
    password = generate_password((string.ascii_lowercase + string.ascii_uppercase + string.punctuation), 15)

    assert (any(c.islower() for c in password)
        and any(c.isupper for c in password)
        and any(string.punctuation for c in password))
    
def test_password_lower_upper_symbol_digit() -> None:
    """ Tests if password returned contains at least one lowercase, one uppercase, one digit, and one symbol. """
    password = generate_password((string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation), 15)

    assert (any(c.islower() for c in password)
        and any(c.isupper for c in password)
        and any(c.isdigit for c in password)
        and any(string.punctuation for c in password))