def _build_auth_header(token: str) -> dict:
    """Build the authorization header."""
    return {"Authorization": f"MediaBrowser Token='{token}'"}
