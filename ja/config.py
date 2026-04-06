from pathlib import Path

BASE_DIR = Path.home() / ".ja"

LOG_PATH = BASE_DIR / "logs.json"
ARCHIVE_PATH = BASE_DIR / "archive"

def ensure_dirs():
    BASE_DIR.mkdir(exist_ok=True)
    ARCHIVE_PATH.mkdir(exist_ok=True)