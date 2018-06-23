import argparse

from googleplay import GmusicApi
from setlistfm import get_last_songs


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Fetch artist songs from setlist.fm and create Google Play Music playlist',
        epilog='''
User credentials for Google Play Music, together (optional now) with setlist.fm API key
are read from a provided credentials.txt file in this format:
    username@gmail.com:password
    last.fm api key\n\n
For the Google credentials either supply the password or a 2-factor API key.

Creates a playlist called "<artist>-today's date".'''
    )
    parser.add_argument('artist', type=str, help='the artist to search for; give exact name')
    arguments = parser.parse_args()

    email, password, setlistFm = read_credentials()
    artist = arguments.artist
    songs = get_last_songs(artist, setlistFm)

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
