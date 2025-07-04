# 🧠 AI Voice Assistant with Python 🎙️

A modular, voice-controlled Python assistant that opens apps, checks dates, manages notes, tells jokes, and logs everything — all using speech recognition and text-to-speech.

---

## 🔧 Features

| Feature               | Description |
|-----------------------|-------------|
| 🎤 Voice Commands     | Speak to interact using `speech_recognition` |
| 🔊 Text-to-Speech     | Assistant replies using `pyttsx3` |
| 🌐 Open Apps          | Opens websites like YouTube, Google, LinkedIn, etc. |
| 📅 Calendar Checker   | Check day/month/year from input date |
| 📓 Notes Manager      | Create, update, delete notes |
| 🤣 AI Jokes           | Tells random jokes (offline) |
| 📈 Usage Analytics    | Tracks how you use each feature |
| 📜 Chat History       | Logs all voice interactions to `logs/chat_history.txt` |

---

## 🗂️ Project Structure

AI-Voice-Assistant/
│
├── assistant.py # Main assistant script
├── features/ # Modular features
│ ├── apps.py
│ ├── calendar_check.py
│ ├── notes.py
│ ├── jokes_ai.py
│ └── analytics.py
├── logs/
│ └── chat_history.txt # Saved command logs
├── analytics/
│ └── analytics_YYYY-MM-DD.json # Usage analytics (auto-created daily)

🙌 Credits
Created by Dev Singh...
