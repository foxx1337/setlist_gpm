### Python setlist.fm - Google Play Music playlist creator

This utility will create Google Play Music playlists to help "get the homework done"
when going to a concert.

The following setup is necessary:
1. Run `pip install -r requirements.txt` (will grab the execellent gmusicapi)
2. Create a file called `credentials.txt` with your Google credentials and
   (now ignored, just put a dummy line there) setlist.fm API key:
   
   ```
   user@gmail.com:application_key
   dummy text here for setlist.fm api
   ```
3. Run this script now:
   ```
   $ python setlist.py "Dream Theater"
   ```
If everything's successful, a new playlist called "Dream Theater-date" should appear
in the Google Play Music account.
