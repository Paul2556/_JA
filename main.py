from dependencies import datetime, json, logs, random
from entry_generation import generate_journal_entry, is_new_day
last_entry_time = json.loads(logs)['last_entry_time']
greetings = [
    "These pages are waiting.",
    "This page is ready for you.",
    "Your journal is open.",
    "This space is yours.",
    "Your thoughts belong here.",
    "The page is yours now.",
    "This moment is yours to write.",
    "Your words have a place here.",
    "The page is ready whenever you are.",
    "This space is here for you.",
    "Your thoughts can rest here.",
    "What's on your mind belongs here.",
    "This is your place to write.",
    "Your thoughts have been waiting.",
    "This page is yours to fill.",
    "Everything you're thinking can go here.",
    "The page is open.",
    "Your space is ready.",
    "This is where your thoughts can land.",
    "You can leave your thoughts here."
]
with open('logs\\logs.json', 'r') as f:
    logs = f.read()
print("""         _   _
        | | / \\
     _  | |/ _ \\
    | |_| / ___ \\
 ____\\___/_/   \\_\\
|_____|
ᵥ.₆""") #! Change the version number ONLY when you make big changes.
if datetime.datetime.now().hour < 12:
	print(f"Good morning, Paul. {greetings[random.randint(0, len(greetings) - 1)]}")
elif datetime.datetime.now().hour < 18:
	print(f"Good afternoon, Paul. {greetings[random.randint(0, len(greetings) - 1)]}")
else:
	print(f"Good evening, Paul. {greetings[random.randint(0, len(greetings) - 1)]}")

try:
	# more than a day so generate new one
	if last_entry_time is None or is_new_day(last_entry_time):
		logs = json.loads(logs)
		logs["entry"] = 1
		json.dump(logs, open('logs\\logs.json', 'w+'), indent=4)
		generate_journal_entry()
		last_entry_time = datetime.datetime.now().timestamp()
	else:
		generate_journal_entry()
except NameError:
	# first time running the program so last_entry_time doesnt exist
	last_entry_time = datetime.datetime.now().timestamp()
	generate_journal_entry()