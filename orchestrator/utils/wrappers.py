### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from functools import wraps

def authenticate(func):
    """Authenticate decorator"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper"""
        #todo: Implement authentication logic
        user_authenticated = True
        if not user_authenticated:
            return {"message": "User is not authenticated to this action"}, 401
        return func(*args, **kwargs)

    return wrapper
