# 🎙️ Jarvis - Python Voice Assistant

A simple **voice-controlled assistant** built with Python that can listen, speak, and perform tasks like opening websites, playing music, and fetching real-time news.

---

## 🚀 Features

* 🎤 Voice recognition using SpeechRecognition
* 🔊 Text-to-speech responses using pyttsx3
* 🌐 Open websites via voice commands
* 🎵 Play songs from a custom music library
* 📰 Fetch latest news using News API
* ⚡ Wake word activation ("Jarvis")

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* requests
* PyAudio

---

## 📦 Installation

### 1. Clone the repository

git clone https://github.com/garvit1226/jarvis-personel-assistant.git
cd jarvis-voice-assistant

### 2. Create virtual environment

python -m venv .venv

### 3. Activate virtual environment

# Windows

.venv\Scripts\activate

# Mac/Linux

source .venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

---

## 🔐 Setup API Key

Create a `config.txt` file in the root directory and add:

NEWS_API_KEY=your_api_key_here

⚠️ Make sure this file is not pushed to GitHub.

Add this to your `.gitignore`:
config.txt

---

## ▶️ Run the Project

python main.py

---

## 🎯 How It Works

1. The assistant listens continuously for the wake word **"Jarvis"**
2. Once activated, it listens for a command
3. Executes tasks like:

   * "Open YouTube"
   * "Play song_name"
   * "Tell me news"

---

## 📁 Project Structure

main.py
musiclib.py
requirements.txt
config.txt (not pushed to GitHub)
README.md

---

## ⚠️ Notes

* Make sure your microphone is working properly
* PyAudio installation may require additional setup (especially on Windows)
* Do not expose your API keys publicly

---

## 🌟 Future Improvements

* Add GUI interface
* Integrate Spotify / YouTube API
* Add more voice commands
* Improve NLP for better understanding

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Inspiration

Inspired by virtual assistants like **Jarvis** from Iron Man 🤖
