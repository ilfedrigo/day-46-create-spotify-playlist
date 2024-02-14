from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year to you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"

CLIENT_ID = "8d66cf5f7cb54a4680aff361f97dbbf8"
CLIENT_SECRET = "8c4f7b24a13b4c308eb38ea49efbab60"

response = requests.get(URL+date)
billboard = response.text
soup = BeautifulSoup(billboard, 'html.parser')

top_100_songs = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in top_100_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, 
                                                           client_secret=CLIENT_SECRET, 
                                                           redirect_uri="https://example.com/", 
                                                           scope="playlist-modify-private",
                                                           username="lucas.fedrigo"))

user_id = sp.current_user()["id"]