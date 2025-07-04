# features/notes.py

import os
import pyttsx3

BASE_NOTES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "features")
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def handle_notes():
    speak("Do you want to create, update, or delete a note?")
    task = input("Enter action: ").lower()

    if "create" in task:
        filename = input("Enter filename (no extension): ")
        content = input("Enter your note content: \n")
        with open(os.path.join(BASE_NOTES, f"notes_{filename}.txt"), 'w') as f:
            f.write(content)
        speak("Note created successfully.")

    elif "update" in task:
        filename = input("Enter filename to update: ")
        path = os.path.join(BASE_NOTES, f"notes_{filename}.txt")
        if os.path.exists(path):
            with open(path, 'a') as f:
                update = input("Enter text to append: ")
                f.write("\n" + update)
            speak("Note updated successfully.")
        else:
            speak("That note doesn't exist.")

    elif "delete" in task:
        filename = input("Enter filename to delete: ")
        path = os.path.join(BASE_NOTES, f"notes_{filename}.txt")
        if os.path.exists(path):
            os.remove(path)
            speak("Note deleted.")
        else:
            speak("Note not found.")

def show_notes():
    files = [f for f in os.listdir(BASE_NOTES) if f.startswith("notes_") and f.endswith(".txt")]
    if not files:
        speak("No notes found.")
    else:
        speak("Here are your notes:")
        for file in files:
            speak(file)
