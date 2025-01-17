### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from functools import wraps


def authenticate(func):
    """
    Authenticate decorator"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper"""

    return wrapper
