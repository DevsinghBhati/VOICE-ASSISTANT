# features/analytics.py

import json
import os
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def load_usage_data(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    else:
        return {
            "total_commands": 0,
            "apps_opened": 0,
            "jokes_told": 0,
            "notes_created": 0,
            "date_checks": 0
        }

def save_usage_data(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def show_report(data):
    speak("Here is your assistant usage report:")
    for key, value in data.items():
        speak(f"{key.replace('_', ' ')}: {value}")

def list_features():
    speak("Here are the features you can access:")
    features = [
        "Open apps and websites",
        "Tell AI-generated jokes",
        "Write, update, and delete notes",
        "Check day, month, or year calendar",
        "View usage analytics and history"
    ]
    for f in features:
        speak(f)
