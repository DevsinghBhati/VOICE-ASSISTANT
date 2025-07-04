# features/jokes_ai.py

import pyttsx3
import random

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_ai_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to therapy? It had too many bytes from the past.",
        "I told my AI assistant a joke, but it just stared at me with a blank expression... classic.",
        "Why was the math book sad? Because it had too many problems.",
        "What do you get when you cross a robot and a tractor? A trans-farmer!",
        "Why did Python break up with JavaScript? Because it couldn’t handle the callbacks."
    ]
    joke = random.choice(jokes)
    speak(joke)
    return joke
