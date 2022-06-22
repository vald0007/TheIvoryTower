from lib2to3.pgen2.literals import test
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

def get_features(song_id):

    meta_data = sp.track(song_id)
    features = sp.audio_features(song_id)
    
    name = meta_data['name']
    artist =  meta_data['album']['artists'][0]['name']
    
    '''
    ==========================================================================================================================
    List of available features - https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features
    ==========================================================================================================================
    danceability 
    energy
    key
    loudness
    mode
    speechiness
    acousticness
    instrumentalness
    liveness
    valence
    tempo
    type
    id
    uri
    track_href
    analysis_url
    duration_ms
    time_signature

    '''
  
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    length = features[0]['duration_ms'] / 1000
    valence = features[0]['valence']

    track = [name, artist,length,danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo]

    return track

    
client_id = ''
client_secret = ''

# I used this article to learn how to do this:
# https://towardsdatascience.com/using-data-visualizations-to-understand-the-vast-shift-from-80s-90s-hip-hop-to-today-afa0f942685

# Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)   

# Get songs' IDs
playlist_uri = ''
user = ''
song_ids = []
playlist = sp.user_playlist(user,playlist_uri)

for item in playlist['tracks']['items']:
    track = item['track']
    song_ids.append(track['id'])
    
#Get  meta_datadata about songs 
tracks = []
for song in song_ids:
    track = get_features(song)
    tracks.append(track)

feature_keys = ['name', 'artist','length','danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
df = pd.DataFrame(tracks,columns = feature_keys)
df.to_csv('TheIvoryTower.csv',index = False)
print('======\nDone\n======')