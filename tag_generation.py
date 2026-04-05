from dependencies import chat, ChatResponse, datetime

with open(f'logs\\archieve\\{datetime.datetime.today().strftime("%Y-%m-%d")}.md', 'r') as f:
    journal_entry = f.read()

response: ChatResponse = chat(model='qwen2.5:7b', messages=[
  {
    'role': 'user',
    'content': f"""
You MUST follow this output format EXACTLY.

OUTPUT FORMAT (NO DEVIATION ALLOWED):
First line: tags (space-separated)
Second line: ---
Then: the original input EXACTLY

If you fail to include tags, your output is WRONG.

---

TASK:
Analyze the journal and assign tags.

INPUT:
\"\"\"{journal_entry}\"\"\"

---

ALLOWED TAGS:
#work, #school, #learning, #technology, #creative, #hobbies, #travel,
#health, #fitness, #mental_health,
#family, #relationships, #friendships, #dating, #social,
#finance,
#goals, #productivity, #routine,
#reflection, #personal_growth, #decisions, #problems, #ideas, #events,
#emotions_positive, #emotions_negative, #emotions_conflict,
#misc

---

CRITICAL RULE:
If the input is mostly:
- testing
- random text
- repeated phrases
- noise / filler

Then output ONLY:
#misc

---

STRICT RULES:
- NEVER skip tags
- NEVER output only the journal
- NEVER add explanations
- ONLY use allowed tags
- 1-5 tags max

---

EXAMPLES:

Input:
testing
hello
yay

Output:
#misc
---
testing
hello
yay

---

Now produce the output.
"""},
])
print(response['message']['content'])