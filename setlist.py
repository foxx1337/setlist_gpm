from gmusicapi import Mobileclient

from setlistfm import get_last_songs


def main():
    songs = get_last_songs('Ghost')
    print(songs)
    # email, password, setlistFm = read_credentials()
    # api = Mobileclient()
    # logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
    # print(logged_in)


def read_credentials():
    with open('credentials.txt', 'r') as f:
        credentials = f.read()
    google, sfm = credentials.strip().split('\n')
    return tuple(google.strip().split(':')) + (sfm, )


if __name__ == '__main__':
    main()
