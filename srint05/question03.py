import re


def valid_email(email: str):
    try:
        if re.match(r'[a-zA-z]+@{1}[^_@]+(\.[a-z]+)+', email) == None:
            raise ValueError
        return 'Email is valid'
    except ValueError:
        return 'Email is not valid'