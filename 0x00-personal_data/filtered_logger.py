#!/usr/bin/env python3

"""THis module contains a function that filter sensitive data
"""


import re


def filter_datum(fields, redaction, message, separator):
    """It filters the a set of personal informations
    return
    """
    for field in fields:
        pattern = re.findall(rf"{field}=(.*?);", message)[0]
        message = re.sub(pattern, "xxx",  message)
    return (message)
