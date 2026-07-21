# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
#
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="bf28268c9a924e3cb715750fd3e78b3a",
#                                                            client_secret="80b707862eae4567ae6afb38d34b4926"))
#
# results = sp.search(q='rekkai m', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= os.getenv('client_id'),
                                               client_secret=os.getenv('client_id'),
                                               redirect_uri="https://www.google.co.in/",
                                               scope="user-library-read"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
####GET ALBUM NAMES WITH ARTIST URI
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#
#
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])

#### how to get 30 second samples and cover art for the top 10 tracks for Led Zeppelin
# lz_uri = 'https://open.spotify.com/artist/5VVN3xZw1i2qihfITZlvCZ?si=FwoXq5fATW6nTp-yg4Nmbg'
# results = spotify.artist_top_tracks(lz_uri)
# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()

# importing the requests library
import requests

# api-endpoint
URL = "https://api.spotify.com/v1/search?q=Muse&type=artist"



# sending get request and saving the response as response object
# r = requests.get(url = URL,params="Authorization: Bearer ")

### getting URI using artist names!!

access_token=''
artist_name='gv prakash'
artist_info = requests.get(
    'https://api.spotify.com/v1/search',
    headers={
        'Authorization': 'Bearer {token}'.format(token=access_token)
    },
    params={ 'q': artist_name, 'type': 'playlist' })
# extracting data in json format
# data = r.json()

data=artist_info.json()

print(artist_info.text)
# for artists
uri=data["playlists"]["items"][0]["uri"]
# for playlist
uri_p=data["playlists"]["items"][0]["id"]
# print(artist_info.text)
# print(uri_p)

# got top playlists with uri
# results = spotify.artist_albums(uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])
###get embed link of artist
# url=data["artists"]["items"][0]["href"]
# embed='https://open.spotify.com/embed/artist/'+url[-22:]+'?utm_source=generator&amp;theme=0'
embed_p='https://open.spotify.com/embed/playlist/'+uri_p+'?utm_source=generator&amp;theme=0'
print(embed_p)
# print(embed)

# url_uri=url+'/si='+uri.split(':')[-1]
url_uri='https://open.spotify.com/embed/artist/'+'5VVN3xZw1i2qihfITZlvCZ'
print(url_uri)

results = spotify.artist_top_tracks(url_uri)
import json
json_object = json.dumps(results, indent = 4)
print(json_object)
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
