import datetime
from ja.config import ARCHIVE_PATH
from ja.log_utils import load_logs, save_logs

def is_new_day(last_entry_time):
    if last_entry_time == 0:
        return True
    last_date = datetime.datetime.fromtimestamp(last_entry_time).date()
    current_date = datetime.datetime.now().date()
    return current_date > last_date

def generate_journal_entry():
    logs = load_logs()
    logs["last_entry_time"] = datetime.datetime.now().timestamp()
    save_logs(logs)
    entry = logs["entry"]
    date_str = datetime.datetime.today().strftime("%Y-%m-%d")
    file_path = ARCHIVE_PATH / f"{date_str}.md"
    print(f"""
=== JOURNAL ENTRY MODE ===

Entry {entry} | {date_str}

Get your thoughts out on the page.
Long or short, it's all good.
Type 'q' on a new line to exit.
""")
    file_path.touch(exist_ok=True)
    first_line = True
    while True:
        line = input("- ").strip()
        if line == "q":
            print("Exiting journal entry mode.\n")
            return "idle"
        if not line:
            continue
        if first_line:
            with open(file_path, 'a') as f:
                f.write(f'\n---\nENTRY {entry}\n---\n\n')
            logs["contents"].append({
                "path": f"{date_str}.md",
                "entry": entry,
                "timestamp": datetime.datetime.now().timestamp()
            })
            logs["entry"] += 1
            first_line = False
        with open(file_path, 'a') as f:
            f.write(line + '\n')
        save_logs(logs)