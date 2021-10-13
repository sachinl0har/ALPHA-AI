# MODULES
import pyttsx3
import datetime
import requests
import speech_recognition as sr
from requests import get

import gui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)
#print(voices[2].id)
#print(voices[3].id)
#print(voices[4].id)
#print(voices[5].id)
#print(voices[6].id)
#print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    gui.speak(audio)
    engine.say(audio)
    engine.runAndWait()
# WISH ME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
      speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Acro Here,How may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

wishMe()

def run_alpha():
        inpu = takeCommand()
        print(inpu)
        url = "http://api.brainshop.ai/get?bid=157984&key=3S0hhLXZ5GS2KYs4&uid=[uid]&msg=[{}]".format(inpu)
        response = requests.get(url).json()['cnt']
        print(response)
        speak(response)

gui.set_speak_command(run_alpha)
gui.mainloop()
