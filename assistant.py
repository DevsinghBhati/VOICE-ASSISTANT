# assistant.py — MAIN RUNNER FILE

from features import apps, analytics, calendar_check, jokes_ai, notes
import speech_recognition as sr
import pyttsx3
import json
import os
from datetime import datetime

# === FOLDER SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "logs", "chat_history.txt")
ANALYTICS_PATH = os.path.join(BASE_DIR, "analytics", f"analytics_{datetime.now().date()}.json")

# === SPEECH SETUP ===
engine = pyttsx3.init()
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        with open(LOG_FILE, "a") as log:
            log.write(f"User: {command}\n")
        return command.lower()
    except:
        speak("Sorry, could you say that again?")
        return ""

# === USAGE ANALYTICS ===
data = analytics.load_usage_data(ANALYTICS_PATH)

# === WELCOME ===
speak("Welcome to your Python AI Voice Assistant!")

# === MAIN LOOP ===
while True:
    command = take_command()
    data['total_commands'] += 1

    if any(x in command for x in ["open", "app", "website"]):
        apps.handle_app(command)
        data['apps_opened'] += 1

    elif "joke" in command or "laugh" in command:
        joke = jokes_ai.get_ai_joke()
        speak(joke)
        data['jokes_told'] += 1

    elif "note" in command or "write" in command:
        notes.handle_notes()
        data['notes_created'] += 1

    elif "calendar" in command or "date" in command:
        calendar_check.handle_calendar()
        data['date_checks'] += 1

    elif "show notes" in command or "list notes" in command:
        notes.show_notes()

    elif "usage" in command or "analytics" in command:
        analytics.show_report(data)

    elif "exit" in command or "quit" in command:
        analytics.save_usage_data(data, ANALYTICS_PATH)
        speak("Goodbye! Have a great day.")
        break

    elif "help" in command or "features" in command:
        analytics.list_features()

    else:
        speak("Sorry, I didn't understand that.")
