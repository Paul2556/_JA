from ollama import chat, ChatResponse
import datetime, keyboard, json, random
from config import LOG_PATH
ARCHIVE_PATH = 'logs\\archive\\'
with open(LOG_PATH, 'r') as f:
    logs = f.read()