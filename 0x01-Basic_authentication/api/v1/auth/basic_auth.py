#!/usr/bin/env python3

"""This is the basic auth module
"""

import base64
import binascii
import models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """This is the basic Auth class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract base64 header
            param: authorization_header
        """

        if not isinstance(authorization_header, str):
            return None
        elif authorization_header is None:
            return None
        elif authorization_header.startswith("Basic "):
            auth_value = authorization_header.split(" ")
            auth_value = auth_value[1]
            return auth_value
        else:
            return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decode base64 header
            param: base_64_authorization_header
        """
        if not isinstance(base64_authorization_header, str):
            return None
        elif base64_authorization_header is None:
            return None
        else:
            result = ""
            try:
                result = base64.b64decode(base64_authorization_header)
                result = result.decode("utf-8")
                return result
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """extract credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if decoded_base64_authorization_header.find(":") == -1:
            return None, None

        values = decoded_base64_authorization_header.split(":")
        return tuple(values)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        get user objects from credentials
        """

        if not isinstance(user_email, str) or user_email is None:
            return None

        if not isinstance(user_pwd, str) or user_str is None:
            return None

        
