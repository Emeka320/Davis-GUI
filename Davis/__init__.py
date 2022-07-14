from datetime import datetime
import pyttsx3
# iimport speech_recognition as sr
import random
import os
import time


engine = pyttsx3.init()


response = ["Yes sir", "Affirmative", "Yes sir", "On it", "Will do"]
res_command = random.choice(response)

query = ['date']

if 'date' in query:
    engine.say("Today's date is" + time.strftime('%A the %d of %B %Y'))
    engine.say(time.strftime('And the time is %H %M '))

hour = datetime.now().hour
if 6 <= hour < 12:
    engine.say("Good Morning Sir")
    engine.runAndWait()

elif 12 <= hour < 18:
    engine.say("Good Afternoon Sir")
    engine.runAndWait()

elif 18 <= hour < 24:
    engine.say("Good Evening Sir")
    engine.runAndWait()
else:
    engine.say("Try and get some sleep Sir")
    engine.runAndWait()

query = ["logout"]

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Sorry Sir, Say that again")
        engine.say("Sorry Sir, Say that again")
        return "None"
    return query

#if 'logout' in query:
    #os.system("shutdown -l")
#if 'shutdown' in query:
    #os.system("shutdown /s /t 1")
#if 'restart' in query:
    #os.system("shutdown /r /t 1")
