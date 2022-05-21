import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
    
client_id = 'client_id'
client_secret = 'client_secret'

# I used this article to learn how to do this:
# https://towardsdatascience.com/using-data-visualizations-to-understand-the-vast-shift-from-80s-90s-hip-hop-to-today-afa0f942685

# Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)   

# Get songs' IDs
playlist_uri = 'uri'
user = 'username'
song_ids = []
playlist = sp.user_playlist(user,playlist_uri)

for item in playlist['tracks']['items']:
    track = item['track']
    song_ids.append(track['id'])
    

#Get metadata about songs FIXME for more than 1 song
meta = sp.track(song_ids[0])
print(meta.keys())
song_attr = sp.audio_features(song_ids[0])
print(song_attr)