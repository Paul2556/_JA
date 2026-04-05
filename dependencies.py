from ollama import chat, ChatResponse
import datetime, keyboard, json, random
with open('logs\\logs.json', 'r') as f:
    logs = f.read()