from dependencies import datetime, json
import idle_mode, keyboard
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
            idle_mode.passive_idle()
        # actual journaling part
        
        with open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'a') as f:
            f.write(f'\n---\nENTRY {entry}\n---\n')
        logs = json.loads(logs)
        logs["entry"] += 1
        json.dump(logs, open('logs\\logs.json', 'w+'), indent=4)
        with open('logs\\logs.json', 'r') as f:
            logs = f.read()
        logs = json.loads(logs)
        logs["contents"].append({"path": f'{datetime.datetime.today().strftime("%Y-%m-%d")}.md', "entry": entry, "timestamp": datetime.datetime.now().timestamp()})
        json.dump(logs, open('logs\\logs.json', 'w+'), indent=4)
        line = input("- ")
        line = line.strip()
        if line and len(line) > 1:            
            with open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'a') as f:
                f.write(line + '\n')
