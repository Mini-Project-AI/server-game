import re

def is_valid_email(email: str) -> bool:
    """
    Checks if the email is valid.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def is_valid_password(password: str) -> bool:
    """
    Checks if the password is valid.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$"
    return re.match(pattern, password) is not None

def is_valid_name(name: str) -> bool:
    """
    Checks if the name is valid.

    Args:
        name (str): The name to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    return len(name) >= 4

def is_valid_age(age: int) -> bool:
    """
    Checks if the age is valid.

    Args:
        age (int): The age to validate.

    Returns:
        bool: True if the age is valid, False otherwise.
    """
    return 6 <= age <= 60
