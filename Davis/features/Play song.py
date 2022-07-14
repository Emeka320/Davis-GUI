import os

query = ["play music"]

if "play music" in query:
    songs_dir = 'C:/Users/chukwuemeka/Music'
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[9]))
