# Top 100 Billboard Generator

## Introduction

Welcome to my 46th day of 100 days of coding with Python! Today let's travel back in time and listen to some good songs

The script utilizes BeautifulSoup for web scraping to extract the top 100 songs from Billboard's Hot 100 chart for a specified date. 

It then interacts with the Spotify API using Spotipy to create a new playlist and add the extracted songs to it.

## Dependencies

1. **BeautifulSoup** is used for web scraping.
2. **requests** is used to make HTTP requests to fetch web pages.
3. **spotipy** is a lightweight Python library for the Spotify Web API.

## Getting Started

1. How it works
2. Prompt the user to input the desired date.
3. Fetch the Billboard Hot 100 chart for the specified date.
4. Extract the titles of the top 100 songs using BeautifulSoup.
5. Authenticate with the Spotify API using SpotifyOAuth.
6. Retrieve the user's Spotify ID.
7. Search for the Spotify URI of each song title.
8. Create a new public playlist on the user's Spotify account with the fetched songs.
9. Add the songs to the created playlist.
