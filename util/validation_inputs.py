import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$"
    return re.match(pattern, password) is not None

def is_valid_name(name):
    return len(name) >= 4

def is_valid_age(age):
    return 6 <= age <= 60
