from googleplay import GmusicApi
from setlistfm import get_last_songs


def main():
    email, password, setlistFm = read_credentials()
    artist = 'Dream Theater'
    songs = get_last_songs(artist)

    api = GmusicApi(email, password)
    api.make_playlist(artist, songs)
    api.close()


def read_credentials():
    with open('credentials.txt', 'r') as f:
        credentials = f.read()
    google, sfm = credentials.strip().split('\n')
    return tuple(google.strip().split(':')) + (sfm, )


if __name__ == '__main__':
    main()
