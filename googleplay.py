import datetime

from gmusicapi import Mobileclient


class GmusicApi:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.api = Mobileclient()
        result = self.api.login(self.email,
                                self.password,
                                Mobileclient.FROM_MAC_ADDRESS)
        print('login for ' + self.email + ': ' + str(result))

    def search(self, query, max_results=50):
        return self.api.search(query, max_results)

    def make_playlist(self, artist, songs):
        song_ids = []
        for song in songs:
            search_result = self.search(artist + ' ' + song)
            if len(search_result['song_hits']) > 0:
                for song_hit in search_result['song_hits']:
                    if song_hit['track']['artist'].lower() == artist.lower():
                        song_ids.append(song_hit['track']['storeId'])
                        break
        playlist_id = self.api.create_playlist(artist + '-'
                                               + str(datetime.datetime.date(datetime.datetime.now())))
        self.api.add_songs_to_playlist(playlist_id, song_ids)

    def close(self):
        self.api.logout()
