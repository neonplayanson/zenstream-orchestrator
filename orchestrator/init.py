### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

import sys

sys.dont_write_bytecode = True

from dotenv import load_dotenv

load_dotenv()

from logger import Logger
from app.app import Orchestrator


if __name__ == "__main__":
    logger = Logger()
    orchestrator = Orchestrator()
    orchestrator.create()
