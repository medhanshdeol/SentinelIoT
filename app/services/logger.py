import logging
from pathlib import Path


Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("SentinelIoT")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("logs/access.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)