### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from .database import DatabaseHandler
from logger import Logger
import os

config = None


class Config:
    def __init__(self, logger: Logger = None):
        self.create_database()

    def create_database(self):
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
        return self._database


def load_config(logger: Logger = None) -> Config:
    global config
    if config is None:
        config = Config(logger=logger)
    return config
