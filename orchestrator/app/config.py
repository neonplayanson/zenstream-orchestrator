### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from .database import DatabaseHandler
from logger import Logger
import os


class Config:
    _instance = None

    def __new__(
        cls,
    ):
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
                        client_tokens JSON NOT NULL
                    )
                """,
                        "columns": {
                            "username": "TEXT UNIQUE NOT NULL",
                            "password": "TEXT NOT NULL",
                            "client_tokens": "JSON NOT NULL",
                        },
                    },
                }
            },
            db_file=os.path.join(os.getcwd(), "sqlite/orchestrator.db"),
        )

        self.database.connect()
        self.database.create_tables()

    @property
    def database(self):
        """Get the database handler."""
        return self._database


config = Config()


def load_config() -> Config:
    """Load the configuration handler."""
    return Config()
