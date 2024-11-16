
from typing import List, TypeVar
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
        pass

    def authorization_header(self, request=None) -> str:
        """give an authorization header to use the api
        """
        if request is None:
            return None

        auth_header = request.headers.get("Authorization")
        print(auth_header)
        if not auth_header:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user of the app
        """
        return None
