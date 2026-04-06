from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

LOG_PATH = BASE_DIR / "logs" / "logs.json"
ARCHIVE_PATH = BASE_DIR / "logs" / "archive"