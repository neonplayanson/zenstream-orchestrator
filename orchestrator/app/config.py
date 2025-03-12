from .database import DatabaseHandler
import os
from hashlib import sha256


class Config:
    _instance = None

    def __new__(
        cls,
    ):
        """Create a new instance of the configuration handler."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)

            cls._instance._initialize()
        return cls._instance

    def _initialize(
        self,
    ):
        """
        Initialize the configuration handler.

        Args:
            logger (Logger): The logger instance.
        """
        self._base_address = {
            "frontend": "http://127.0.0.1:3000",
            "backend": "http://127.0.0.1:5090"
        }

        self.create_database()

    def create_database(self):
        """Create the database handler."""
        if os.path.exists(os.path.join(os.getcwd(), "sqlite")) is False:
            os.makedirs(os.path.join(os.getcwd(), "sqlite"))
        self._database = DatabaseHandler(
            db_type="sqlite",
            create_query={
                "sqlite": {
                    "users": {
                        "create": """
                    CREATE TABLE IF NOT EXISTS users (
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                    )
                """,
                        "columns": {
                            "username": "TEXT UNIQUE NOT NULL",
                            "password": "TEXT NOT NULL",
                        },
                    },
                    "invites": {
                        "create": """
                        CREATE TABLE IF NOT EXISTS invites (
                            url TEXT UNIQUE NOT NULL
                            )""",
                        "columns": {"url": "TEXT UNIQUE NOT NULL"},
                    },
                    "settings": {
                        "create": """
                        CREATE TABLE IF NOT EXISTS settings (
                            servername TEXT NOT NULL, 
                            origin_type INTEGER NOT NULL,
                            origin_url TEXT NOT NULL,
                            api_key TEXT NOT NULL
                        )
                        """,
                        "columns": {
                            "servername": "TEXT NOT NULL",
                            "origin_type": "INTEGER NOT NULL",
                            "origin_url": "TEXT NOT NULL",
                            "api_key": "TEXT NOT NULL",
                        },
                    },
                    "client_secrets": {
                        "create": """
                        CREATE TABLE IF NOT EXISTS client_secrets (
                            username TEXT NOT NULL,
                            client_secret TEXT NOT NULL,
                            expiration TEXT NOT NULL
                        )""",
                        "columns": {
                            "username": "TEXT NOT NULL",
                            "client_secret": "TEXT NOT NULL",
                            "expiration": "TEXT NOT NULL",
                        },
                    },
                },
            },
            db_file=os.path.join(os.getcwd(), "sqlite/orchestrator.db"),
        )

        self.database.connect()
        self.database.create_tables()
        self.database.execute(
            "INSERT OR IGNORE INTO users VALUES ('admin', ?)",
            (sha256("admin".encode()).hexdigest(),),
        )

    @property
    def database(self):
        """Get the database handler."""
        return self._database

    @property
    def base_address(self):
        """Get the base address configuration."""
        return self._base_address


config = Config()


def load_config() -> Config:
    """Load the configuration handler."""
    return Config()
