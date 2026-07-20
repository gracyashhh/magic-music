import requests
import base64
import json
import os
import urllib.request
#######VERY IMPORTANT TO CODE TO GET PAST THE *EVERY 1 HOUR EXPIRING ACCESS TOKEN*####
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}
client_id="bf28268c9a924e3cb715750fd3e78b3a"
client_secret="80b707862eae4567ae6afb38d34b4926"
redirect_uri="https://www.google.co.in/"
message = f"{client_id}:{client_secret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Step 2 - Use Access Token to call playlist endpoint
headers = {
    "Authorization": "Bearer " + token
}
###### get name of song track and fetch url of img ####
artist_name='kanneriley'

artist_info = requests.get(
    'https://api.spotify.com/v1/search',
    headers=headers,
    params={ 'q': artist_name, 'type': 'track' })
data=artist_info.json()
# print(artist_info.text)
# uri=data["playlists"]["items"][0]["uri"]
# for playlist
# uri_p=data["playlists"]["items"][0]["id"]
total=len(data["tracks"]["items"])
for z in range(total):
    uri_p = data["tracks"]["items"][z]["album"]["images"][0]["url"]
    parent_dir="F:\Projects-of-all-time\Music-player\song-images\\"
    directory=artist_name
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except:
        pass
    # playlistId = "0PedzRv5oaVHXOXJzhA01t"
    # playlistId=uri_p
    # playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}/images"

    # res = requests.get(url=playlistUrl, headers=headers)
    #
    # op=json.dumps(res.json(), indent=2)
    # print(op)
    # precious_link=json.loads(op)[0]["url"]

    urllib.request.urlretrieve(uri_p, f"F:\Projects-of-all-time\Music-player\song-images\\{artist_name}\\{artist_name}-{z}.jpg")