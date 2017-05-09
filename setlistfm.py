import requests


def get_setlists(artist):
    r = requests.get('http://api.setlist.fm/rest/0.1/search/setlists?artistName=' + artist, headers={'Accept': 'application/json'})
    return r.json()


def get_last_songs(artist):
    result = get_setlists(artist)
    setlist = result['setlists']['setlist']
    for event in setlist:
        if event['sets']:
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
                    songs += [song['@name'] for song in songparts]
            return songs
