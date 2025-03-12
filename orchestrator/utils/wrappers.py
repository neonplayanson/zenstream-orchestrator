from functools import wraps
from app.config import Config
from flask import request
import json


def authenticate(func):
    """
    Authenticate decorator to ensure that the user is authenticated before
    executing the decorated function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function with authentication check.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to check user authentication.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            function: The original function if the user is authenticated.
            dict: A message indicating the user is not authenticated with a 401 status code.
        """
        try:
            token = request.headers.get("TOKEN")
            user = request.headers.get("Username")
            if not token or not user:
                return {"message": "Username or Token not found"}, 401

            db = Config()._database
            result = db.execute(
                "SELECT client_tokens FROM users WHERE username = ?", (user,)
            )
            if not result:
                return {"message": "User not found"}, 403

            tokens = json.loads(result[0][0])
            if not any(token in v for v in tokens.values()):
                return {"message": "Invalid token"}, 403

            return func(*args, **kwargs)

        except Exception as e:
            print(f"Authentication error: {e}")
            return {"message": "Authentication failed"}, 403

    return wrapper
