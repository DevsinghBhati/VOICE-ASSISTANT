# features/calendar_check.py

import calendar
from datetime import datetime
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def handle_calendar():
    speak("Do you want to check day, month, or year?")
    choice = input("Enter your choice: ").lower()

    try:
        if "day" in choice:
            d = int(input("Enter day (1-31): "))
            m = int(input("Enter month (1-12): "))
            y = int(input("Enter year (e.g., 2025): "))
            date = datetime(y, m, d)
            speak(f"That was a {date.strftime('%A')}")

        elif "month" in choice:
            m = int(input("Enter month (1-12): "))
            y = int(input("Enter year: "))
            cal = calendar.month(y, m)
            print(cal)
            speak("Here is your calendar.")

        elif "year" in choice:
            y = int(input("Enter year: "))
            print(calendar.calendar(y))
            speak("Here is the full year calendar.")

        else:
            speak("Invalid choice.")

    except ValueError:
        speak("Invalid date input.")
