#!/usr/bin/env python3

"""THis module contains a function that filter sensitive data
"""


import re


def filter_datum(fields, redaction, message, separator):
    """It filters the a set of personal informations
    return
    """
    for field in fields:
        try:
            pattern = re.findall(rf"{field}=(.*?){separator}", message)[0]
        except IndexError:
            pattern = ""
        message = re.sub(pattern, "xxx",  message)
    return (message)


import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        self.fields = fields
        super(RedactingFormatter, self).__init__(
                self.format(self.FORMAT))

    def format(self, record: logging.LogRecord) -> str:
        result = filter_datum(self.fields, RedactingFormatter.REDACTION,
                              record, RedactingFormatter.SEPARATOR)
        return result
