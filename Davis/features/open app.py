import os

query = ["open app"]

if 'open app' in query:
    os.system('explorer C://{}'.format(query.replace('Open', '')))
