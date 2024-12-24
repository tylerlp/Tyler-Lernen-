import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import webbrowser

# Spotify API-Zugangsdaten
client_id = ''
client_secret = 'S'

# Spotify-Authentifizierung
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def find_song_and_open_in_browser(song_name, artist_name):
    # Suche nach einem Track auf Spotify
    query = f"track:{song_name} artist:{artist_name}"
    result = sp.search(q=query, type='track', limit=1)  # Suche den ersten Treffer
    
    tracks = result['tracks']['items']
    
    if tracks:
        track = tracks[0]
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album = track['album']['name']
        spotify_url = track['external_urls']['spotify']
        
        print(f"Gefundener Song: {track_name}, Künstler: {artists}, Album: {album}")
        print(f"Öffne Spotify-Link: {spotify_url}")
        
        # Öffne den Song-Link im Standard-Webbrowser
        webbrowser.open(spotify_url)
    else:
        print("Keine Treffer gefunden.")

# Beispielaufruf
song_name = input("Gib den Namen des Songs ein: ")
artist_name = input("Gib den Namen des Künstlers ein: ")

find_song_and_open_in_browser(song_name, artist_name)
