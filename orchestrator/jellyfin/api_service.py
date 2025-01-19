### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================


def _build_auth_header(token: str) -> dict:
    """Build the authorization header."""
    return {"Authorization": f"MediaBrowser Token='{token}'"}


