import json
from ja.config import LOG_PATH, ensure_dirs

def init_logs():
    ensure_dirs()

    if not LOG_PATH.exists():
        with open(LOG_PATH, 'w') as f:
            json.dump({
                "last_entry_time": 0,
                "entry": 1,
                "contents": []
            }, f, indent=4)

def load_logs():
    with open(LOG_PATH, 'r') as f:
        return json.load(f)

def save_logs(logs):
    with open(LOG_PATH, 'w') as f:
        json.dump(logs, f, indent=4)