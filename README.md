### Python setlist.fm - Google Play Music playlist creator

This utility will create Google Play Music playlists to help "get the homework done"
when going to a concert.

The following setup is necessary:

1. Run `pip install -r requirements.txt` (will grab the execellent gmusicapi)

2. Create a file called `credentials.txt` with your Google credentials and
   the setlist.fm API key: 
   ```
   user@gmail.com:application_key
   setlist.fm api key
   ```
   
   The setlist.fm API key can be found at
   [https://www.setlist.fm/settings/api/your-username](https://www.setlist.fm/settings/api/your-username).
   
3. Run the script now, with an artist name as argument:

   ```
   $ python setlist.py "Dream Theater"
   ```

If everything's successful, a new playlist called "Dream Theater-date" should appear
in your Google Play Music account.
