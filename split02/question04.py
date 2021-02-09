import re


def pretty_message(data):
    return  re.sub(r'(.|.{2}|.{3})\1+', r'\1', data)