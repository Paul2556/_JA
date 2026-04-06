import datetime
import random
from journal import generate_journal_entry, is_new_day
from idle import passive_idle
from log_utils import init_logs, load_logs, save_logs
import textwrap
def main():
	init_logs()
	logs = load_logs()
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
	LOGO = """
        _   _
       | | / \\
    _  | |/ _ \\
   | |_| / ___ \\
____\\___/_/   \\_\\
|_____|
ᵥ.₇
""" #! change the v AND change the version within setup when you update the version number. I know, it's a pain, but still, do it  >:). Also only do it when there is signifigant changes, or else just do like .x.x update.

	print(textwrap.dedent(LOGO))
	hour = datetime.datetime.now().hour
	greeting = random.choice(greetings)
	if hour < 12:
		print(f"Good morning, Paul. {greeting}")
	elif hour < 18:
		print(f"Good afternoon, Paul. {greeting}")
	else:
		print(f"Good evening, Paul. {greeting}")
	if is_new_day(logs["last_entry_time"]):
		print("A new day has begun since your last entry.")
		logs["entry"] = 1
		save_logs(logs)
	state = "journal"
	while True:
		if state == "journal":
			state = generate_journal_entry()

		elif state == "idle":
			state = passive_idle()

		elif state == "exit":
			break

if __name__ == "__main__":
	main()