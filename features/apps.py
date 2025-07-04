# features/apps.py

import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def handle_app(command):
    speak("Which app or website would you like to open?")
    app = input("App name (or say something): ").lower()

    if "youtube" in app:
        webbrowser.open("https://www.youtube.com")
    elif "instagram" in app:
        webbrowser.open("https://www.instagram.com")
    elif "facebook" in app:
        webbrowser.open("https://www.facebook.com")
    elif "linkedin" in app:
        webbrowser.open("https://www.linkedin.com")
    elif "google" in app or "chrome" in app:
        webbrowser.open("https://www.google.com")
    elif "github" in app:
        webbrowser.open("https://www.github.com")
    elif "stackoverflow" in app:
        webbrowser.open("https://stackoverflow.com")
    else:
        webbrowser.open(f"https://www.{app}.com")

    speak(f"Opening {app}")
