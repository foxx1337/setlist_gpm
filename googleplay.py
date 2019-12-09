import datetime

from gmusicapi import Mobileclient
from os.path import isfile


class GmusicApi:
    OAUTH_FILE = "gpm.json"

    def __init__(self):
        self.api = Mobileclient()
        if not isfile(GmusicApi.OAUTH_FILE):
            self.oauth = self.api.perform_oauth(GmusicApi.OAUTH_FILE)

        could_login = self.api.oauth_login(Mobileclient.FROM_MAC_ADDRESS, GmusicApi.OAUTH_FILE)

    def search(self, query, max_results=50):
        return self.api.search(query, max_results)

    def make_playlist(self, artist, songs):
        song_ids = []
        show_id = 1
        playlist_id = 1

        for song in songs:
            search_result = self.search(artist + ' ' + song)
            if len(search_result['song_hits']) > 0:
                song_id, album, title = self.first_album_song(search_result['song_hits'], artist)
                if song_id:
                    song_ids.append(song_id)
                    print('{:02}/{:02}{:>32} - {}: {}'.format(playlist_id, show_id, song, album, title))
                    playlist_id += 1
                else:
                    print('{:02}   {:>32} - ?'.format(show_id, song))
            show_id += 1

        playlist_id = self.api.create_playlist(artist + '-'
            + str(datetime.datetime.date(datetime.datetime.now())))
        self.api.add_songs_to_playlist(playlist_id, song_ids)

    def first_album_song(self, song_hits, artist):
        candidate = (None, None, None)
        for song_hit in song_hits:
            if song_hit['track']['artist'].lower() == artist.lower():
                if not self.is_low_quality(song_hit['track']['title']):
                    return (song_hit['track']['storeId'],
                        song_hit['track']['album'],
                        song_hit['track']['title'])
                elif not candidate:
                    candidate = (song_hit['track']['storeId'],
                        song_hit['track']['album'],
                        song_hit['track']['title'])

        return candidate

    def is_low_quality(self, song):
        title = song.lower()
        return (('(live' in title)
            or ('edit)' in title)
            or ('remix' in title))

    def close(self):
        self.api.logout()
