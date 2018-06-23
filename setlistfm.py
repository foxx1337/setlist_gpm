import requests


def get_setlists(artist, api_key):
    r = requests.get('https://api.setlist.fm/rest/1.0/search/setlists?artistName=' + artist, headers={'Accept': 'application/json', 'x-api-key': api_key})
    return r.json()


def get_last_songs(artist, api_key):
    result = get_setlists(artist, api_key)
    setlist = result['setlist']
    for event in setlist:
        if event['sets'] and len(event['sets']['set']) > 0:
            parts = event['sets']['set']
            songs = []
            if type(parts) == dict:
                # wrap it in a list so that the code afterwards works in this case too
                parts = [parts]
            # since everything's a list now...
            for part in parts:
                songparts = part['song']
                if type(songparts) == dict:
                    songs.append(songparts['@name'])
                else:
                    # it's a list
                    songs += [song['name'] for song in songparts]
            return songs
