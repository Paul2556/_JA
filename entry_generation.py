from dependencies import datetime, keyboard, json
def generate_journal_entry():
    with open('logs\\logs.json', 'r') as f:
        logs = f.read()
    entry = json.loads(logs)['entry']
    print(f"""
=== JOURNAL ENTRY MODE ===

Entry {entry} | {datetime.datetime.today().strftime("%Y-%m-%d")}

Get your thoughts out on the page. 
Long or short, it's all good. 
(Type 'q' on a new line to exit)
""")
    try:
        with open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'r') as f:
            pass
    except (FileNotFoundError, OSError):
        open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'x')
    while True:
        # stuff for exiting
        if keyboard.is_pressed('q'):
            print("Exiting journal entry mode.")
            with open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'a') as f:
                f.write(f'\n---\nENTRY {entry}\n---\n')
            logs = json.loads(logs)
            logs["entry"] += 1
            json.dump(logs, open('logs\\logs.json', 'w+'), indent=4)
            with open('logs\\logs.json', 'r') as f:
                logs = f.read()
            logs = json.loads(logs)
            print(logs)
            logs["contents"].append({"path": f'{datetime.datetime.today().strftime("%Y-%m-%d")}.md', "entry": entry, "timestamp": datetime.datetime.now().timestamp()})
            json.dump(logs, open('logs\\logs.json', 'w+'), indent=4)

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
                elif line == "q":
                    print("Hoping to see you again soon, Paul. Goodbye!")
                    exit()
        # actual journaling part
        
        line = input("- ")
        line = line.strip()
        if line and len(line) > 1:            
            with open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'a') as f:
                f.write(line + '\n')
