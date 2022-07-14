import os

query = ["clock out"]

if 'logout' in query:
    os.system("shutdown -l")
if 'clock out' in query:
    os.system("shutdown /s /t 1")
if 'restart' in query:
    os.system("shutdown /r /t 1")
