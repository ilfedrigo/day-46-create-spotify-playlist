from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year to you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"

CLIENT_ID = ""
CLIENT_SECRET = ""
APP_URI = "https://example.com/"
response = requests.get(URL+date)
billboard = response.text
soup = BeautifulSoup(billboard, 'html.parser')

top_100_songs = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in top_100_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth
                                    (
                                    client_id=CLIENT_ID, 
                                    client_secret=CLIENT_SECRET, 
                                    redirect_uri=APP_URI, 
                                    scope="playlist-modify-public",
                                    username="lucas.fedrigo"
                                    )
                    )

user_id = sp.current_user()["id"]

uris = [sp.search(title)["tracks"]["items"][0]["uri"] for title in song_list]

# Create playlist:
playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} - Billboard 100", public=True, description='')['id']

# Insert Tracks on Playlist
sp.user_playlist_add_tracks(playlist_id=playlist_id, tracks=uris, user=user_id)
