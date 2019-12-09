import argparse

from googleplay import GmusicApi
from setlistfm import get_last_songs


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Fetch artist songs from setlist.fm and create Google Play Music playlist',
        epilog='''
User credentials for Google Play Music are stored in gpm.json and retrieved via browser here.
Optional now setlist.fm API key is read from a provided credentials.txt file in this format:
    last.fm api key\n\n

Creates a playlist called "<artist>-today's date".'''
    )
    parser.add_argument('artist', type=str, help='the artist to search for; give exact name, don\'t fear quotes')
    arguments = parser.parse_args()

    setlistFm = read_credentials()
    artist = arguments.artist
    songs = get_last_songs(artist, setlistFm)

    api = GmusicApi()
    api.make_playlist(artist, songs)
    api.close()


def read_credentials():
    with open('credentials.txt', 'r') as f:
        credentials = f.read()
    return credentials.strip().split('\n')[0]


if __name__ == '__main__':
    main()
