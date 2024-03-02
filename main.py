# Importing Necessary Libraries
from pygame import mixer
import time
import pyttsx3
import datetime
import speech_recognition as sr
from getpass import getpass
from requests import get


# Set tone for listening
mixer.init()
mixer.music.load("ringtone.mpeg")
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
    speak("I am Gemini, Your Virtual Assistant 1.0.1 Please tell me how may I help you")
    time.sleep(2)
'''
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
'''
def take_gemini_command():
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source,duration=1)
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Recognizing..........")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Timeout waiting for speech input.")
            return "None"
        except sr.UnknownValueError:
            print("Unable to recognize speech.")
            return "None"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "None"




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
