import PySimpleGUI as sg
import os

Input = sg.InputText()
layout = [
    [sg.Text("Enter a Command") , Input],
    [sg.Button("OK") , sg.Button('Cancel')]
]
window = sg.Window("Davis", layout)

if  Input == "play music":
    songs_dir = 'C:/Users/chukwuemeka/Music'
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[9]))



while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

window.close()