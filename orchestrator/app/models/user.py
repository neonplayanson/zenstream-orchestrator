from datetime import datetime, timedelta
from hashlib import sha256
from app.config import Config
from app.modules.token import Token


class User:
    def __init__(self, username: str, password: str = None):
        self.username = username
        self.password = sha256(password.encode()).hexdigest() if password else None
        self._db = Config()._database

    def authenticate(self, token: str) -> bool:
        """Authenticate user with token"""
        self._db.execute("""
            DELETE FROM client_secrets
            WHERE username = ?
            AND datetime(expiration) < datetime('now')
        """, (self.username,))

        check = self._db.execute(
            "SELECT client_secret FROM client_secrets WHERE username = ?",
            (self.username,),
        )
        print(check)

        return bool(check and check[0][0] == token)

    def register(self, inviteid: str) -> tuple[bool, bool]:
        """Register new user with invite"""
        if not self._db.execute("SELECT * FROM invites WHERE url = ?", (inviteid,)):
            return False, True

        try:
            self._db.execute(
                "INSERT INTO users VALUES (?, ?, '{}')",
                (self.username, self.password),
            )
            return True, False
        except Exception:
            return False, False

    def login(self, password: str) -> str | bool:
        """Login user and return token"""
        check = self._db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (self.username, password),
        )

        if check:
            self._db.execute("""
            DELETE FROM client_secrets
            WHERE username = ?
            AND datetime(expiration) < datetime('now')
            """, (self.username,))

            token = Token.generate_token()

            self._db.execute(
                "INSERT INTO client_secrets VALUES (?, ?, ?)",
                (self.username, token, str(datetime.now() + timedelta(days=7))),
            )
            return token
        return False

    def logout(self, token: str) -> bool:
        """Logout user by removing token"""
        operation = self._db.execute(
            "DELETE FROM client_secrets WHERE client_secret = ?",
            (token,),
        )
        
        if operation:
            return True
        return False

    def info(self) -> dict:
        """Return user info"""
        try:
            data = self._db.execute(
                "SELECT * FROM users WHERE username = ?",
                (self.username,),
            )
            return {
                "username": data[0][0],
                "password": data[0][1],
            }
        except Exception:
            return {}
