import spotipy
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# 1. Enter your specific credentials here
CLIENT_ID = '93b629c6d9f7451eab1c772c836d04b2'
CLIENT_SECRET = 'b0d8a21127a8426f9b28e7d97106aeff'

# We request permission to read data AND create/modify public playlists
scope = "playlist-modify-public"

# 2. Log into Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:9000",
    scope=scope
))

print("Successfully connected to the Spotify API!\n")

# 3. Let's test it by searching for a song that ISN'T in your CSV
search_query = "Flowers Miley Cyrus"
results = sp.search(q=search_query, limit=1, type='track')

# Extract the Track ID
track_data = results['tracks']['items'][0]
track_name = track_data['name']
track_id = track_data['id']
artist_name = track_data['artists'][0]['name']

print(f"Found: {track_name} by {artist_name} (ID: {track_id})")

# 4. Fetch the live mathematical audio features for that specific ID
live_features = sp.audio_features(track_id)[0]

# Print them out to see the math!
print(f"Energy: {live_features['energy']}")
print(f"Danceability: {live_features['danceability']}")
print(f"Tempo: {live_features['tempo']}")