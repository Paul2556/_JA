import datetime
from ja.journal import generate_journal_entry
from ja.log_utils import load_logs
from ja.config import ARCHIVE_PATH

def find_entry():
    logs = load_logs()
    print("Flipping through the pages...")
    unique_files = {}
    for item in logs["contents"]:
        unique_files[item["path"]] = item["timestamp"]
    files = list(unique_files.items())
    files.sort(key=lambda x: x[1], reverse=True)
    for i, (path, timestamp) in enumerate(files, start=1):
        time_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        print(f"[{i}] {path} | {time_str}")
    print("Enter the number of the entry you want to view:")
    line = input("> ").strip()
    if line.isdigit():
        index = int(line) - 1
        if 0 <= index < len(logs["contents"]):
            entry = logs["contents"][index]
            print("\n=== Reading the page... ===\n")
            with open(ARCHIVE_PATH / entry['path'], 'r') as f:
                print(f.read())
            return
    print("Invalid entry number.")

def passive_idle():
    while True:
        logs = load_logs()
        entry = logs["entry"]
        print(f"""
=== IDLE MODE ===

COMMANDS:
[j] Start new journal entry (current entry: {entry})
[s] View past journal entries
[q] Quit program
Enter command:
""")
        cmd = input("> ").strip()
        if cmd == "j":
            print("Turning the pages...")
            return "journal"
        elif cmd == "s":
            find_entry()
        elif cmd == "q":
            print("Hoping to see you again soon, Paul. Goodbye!")
            return "exit"