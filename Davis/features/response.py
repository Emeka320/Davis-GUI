import pyttsx3
import random
engine = pyttsx3.init()

response = ["Yes sir", "Affirmative", "Yes sir", "On it", "Will do"]
res_command = random.choice(response)
engine.say(res_command)
engine.runAndWait()
