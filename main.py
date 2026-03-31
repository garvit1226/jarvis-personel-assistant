# .\.venv\Scripts\python.exe main.py

import speech_recognition as sr
import webbrowser 
import pyttsx3
import musiclib
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) 
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    # open a platform
    if c.lower().startswith("open"):
        platform = c.split(" ",1)
        if len(platform)<2:
            speak("Please tell me the platform name.")
            return
        app = platform[1]
        speak(f"opening {app}")
        webbrowser.open(f"https://www.{app}.com/")


    # play song
    elif c.lower().startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) < 2:
            speak("Please tell me the song name.")
            return

        song = parts[1] 
        link = musiclib.music.get(song.lower())

        if link:
            speak(f"playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found.")

    # news using api 
    elif "news" in c.lower():
        print("Fetching news...")
        try:
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={config.NEWS_API_KEY}"
            a = requests.get(url, timeout=10)
            data = a.json()

            articles = data.get("articles", [])

            if not articles:
                url = "https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&language=en&apiKey={config.NEWS_API_KEY}"
                a = requests.get(url, timeout=10)
                data = a.json()
                articles = data.get("articles", [])

            if not articles:
                speak("Sorry, no news articles are available right now.")
                return

            for article in articles[:5]:
                title = article.get("title", "No title")
                print(title)
                speak(title)

        except Exception as e:
            print("News error:", e)
            speak("There was an error fetching news.")


    # else 
    else:
        speak("Sorry I was unable to understand your voice. Please speak again")

if __name__ == "__main__":
    speak("Initializing jarvis........")
    while True:
        # listen for the wake word jarvis
        r = sr.Recognizer()
        
        
        print("recognizing....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("yess")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)
        
        except Exception as e:
            print("Error; {0}".format(e))