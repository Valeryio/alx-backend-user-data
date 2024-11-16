
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
        return False

    def authorization_header(self, request=None) -> str:
        """give an authorization header to use the api
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user of the app
        """
        return None
