### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from functools import wraps


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass

    return wrapper
