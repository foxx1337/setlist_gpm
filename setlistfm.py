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
            for part in parts:
                songs += [song['@name'] for song in part['song']]
            return songs
