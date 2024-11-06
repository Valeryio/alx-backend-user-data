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
    """
    all_messages = message.split(";")
    all_messages.pop(-1)

    for i in range(len(all_messages)):
        data_array = all_messages[i].split("=")
        all_messages[i] = {data_array[0]: data_array[1]}

    for i in all_messages:
        for key, value in i.items():
            if key in fields:
                i[key] = redaction
    """
    return (message)
