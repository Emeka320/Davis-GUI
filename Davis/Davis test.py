import PySimpleGUI as sg
import os

Input = sg.InputText()
layout = [
    [sg.Text("Enter a Command") , Input],
    [sg.Button("OK") , sg.Button('Cancel')]
]
window = sg.Window("Davis", layout)

while True:
    event, values = window.read()
    if "play music" in Input:
        songs_dir = 'C:/Users/chukwuemeka/Music'
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[9]))
    elif 'logout' in Input:
        os.system("shutdown -l")
    elif 'clock out' in Input:
        os.system("shutdown /s /t 1")
    elif 'restart' in Input:
        os.system("shutdown /r /t 1")
    if event in (None, 'Cancel'):
        break

window.close()