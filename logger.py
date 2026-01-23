# logger.py

import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    f"voice_ai_{datetime.now().strftime('%Y-%m-%d')}.log"
)

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File output (rotates at 5MB)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
