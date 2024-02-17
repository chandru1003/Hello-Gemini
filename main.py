# Importing Necessary Libraries
from pygame import mixer
import wolframalpha
import time
import requests
import pyttsx3
import datetime
import wikipedia
import os
import webbrowser
import cv2
import random
import pyjokes
import speech_recognition as sr
from getpass import getpass
from requests import get

# Counter for password attempts
i = 1

# Set tone for listening
mixer.init()
mixer.music.load("demo.mpeg")
mixer.music.set_volume(0.7)

# Voices based Command
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function for speaking audio
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

# Function for greeting
def wish_gemini():
    speak("Initializing Gemini")
    time.sleep(2)
    hour = int(datetime.datetime.now().hour)
    
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    date_time2 = datetime.datetime.now().strftime("%d %b %Y %I:%M %p")
    time.sleep(2)
    speak(f"It's {date_time2}")
    time.sleep(2)
    speak("I am Gemini, Your Virtual Assistant 2.2.0. Please tell me how may I help you")
    time.sleep(2)

# Function for taking command from user
def take_gemini_command():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=10)
    
    try:
        mixer.music.play()
        print("Recognizing..........")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
        time.sleep(2)
        mixer.music.stop()
    
    except Exception as e:
        print("Sorry about that, I didn't hear anything. Say that again, please.....")
        return "None"
    
    return query

# List of supported functions
supported_functions = [wish_gemini, take_gemini_command]

# Main function
if __name__ == '__main__':
    wish_gemini()
    
    while True:
        user_command = take_gemini_command().lower()
        
        for func in supported_functions:
            if func.__name__.lower() in user_command:
                func()
                break
