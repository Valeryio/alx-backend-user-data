
from typing import List
from flask import request

"""THis module contains an auth class
"""


class Auth:
    """This is an authentication customized
    class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authorization verifier
        """
        if path is not None and path[-1] != "/":
            path += "/"

        if excluded_paths == [] or excluded_paths is None:
            return True

        if path is None or path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """give an authorization header to use the api
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user of the app
        """
        return None
