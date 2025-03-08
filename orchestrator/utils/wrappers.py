### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from functools import wraps
from app.config import Config
from flask import request


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
        except Exception:
            return {"message": "Username or Token not found"}, 401

        db = Config()._database
        check = db.execute(
            "SELECT * FROM users WHERE username = ? AND client_tokens LIKE ?",
            (user, f"%{token}%"),
        )
        if check:
            return func(*args, **kwargs)
        return {"message": "User is not authenticated to this action"}, 403

    return wrapper
