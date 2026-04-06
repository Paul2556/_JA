from dependencies import datetime, keyboard, json
from entry_generation import generate_journal_entry
with open('logs\\logs.json', 'r') as f:
    logs = f.read()
entry = json.loads(logs)['entry']
def find_entry():
    print("Flipping through the pages...")
    i = 0
    for item in logs["contents"]:
        i += 1
        print(f"[{i}] Entry {item['entry']} | {datetime.datetime.fromtimestamp(item['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
    print("Enter the number of the entry you want to view:")
    line = input("> ")
    line = line.strip()
    if line.isdigit() and 1 <= int(line) <= len(logs["contents"]):
        print("\n=== Reading the page... === \n")
        entry_to_view = logs["contents"][int(line) - 1]
        with open(f'logs\\archieve\\{entry_to_view["path"]}', 'r') as f:
            print(f.read())
    else:
        print("Invalid entry number.")
def passive_idle():
    while True:
            print(f"""
        === IDLE MODE ===

        COMMANDS:
        [j] Start new journal entry (current entry: {entry + 1})
        [s] View past journal entries
        [q] Quit program
        Enter command:
        """)
            line = input("> ")
            line = line.strip()
            if line == "j":
                print("Turning the pages...")
                generate_journal_entry()
            elif line == "s":
                find_entry()
            elif line == "q":
                print("Hoping to see you again soon, Paul. Goodbye!")
                exit()