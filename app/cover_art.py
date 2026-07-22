import requests
import base64
import traceback
import sys
import threading
from random import randint
#######VERY IMPORTANT TO CODE TO GET PAST THE *EVERY 1 HOUR EXPIRING ACCESS TOKEN*######
# STILL FACING SAME , FIND A WAY ASAP!!
# 'tracks' ugh {'error': {'status': 401, 'message': 'The access token expired'}}
# Traceback (most recent call last):
#   File "F:\Projects-of-all-time\Music-player\app\cover_art.py", line 139, in get_cover_art
#     uri_p = data["tracks"]["items"][0]["album"]["images"][0]["url"]
# KeyError: 'tracks'
#  whatever
# <traceback object at 0x00000232C604DB80> wth

import threading
import os
from dotenv import load_dotenv

if getattr(sys, "frozen", False):
    env_path = os.path.join(sys._MEIPASS, ".env")
else:
    env_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ".env"
    )

load_dotenv(env_path)
cc=0
def get_rid():
    global headers,cc
    cc+=1
    threading.Timer(60.0*3, get_rid).start()
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}
    # client_id_old = os.getenv('client_id_old')
    client_id = os.getenv('client_id') #new one with premium
    # client_secret_old = os.getenv('client_secret_old')
    client_secret = os.getenv('client_secret')
    redirect_uri = "https://www.google.co.in/"
    message = f"{client_id}:{client_secret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"
    r = requests.post(url, headers=headers, data=data)
    print("Status:", r.status_code)
    print("Response:", r.text)
    response = r.json()

    if 'access_token' not in response:
        print("Spotify authentication failed:", response)
        return
    # token = r.json()['access_token']
    token = response['access_token']
    headers = {
        "Authorization": "Bearer " + token
    }
    print('authorized on key ',cc)

get_rid()

backup_imgs=["https://cdn.pixabay.com/photo/2016/11/23/00/43/audio-1851517_960_720.jpg",
             "https://cdn5.vectorstock.com/i/1000x1000/48/89/love-music-neon-sign-vector-22884889.jpg",
             "https://images.pexels.com/photos/668295/pexels-photo-668295.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
             "https://images.pexels.com/photos/2769274/pexels-photo-2769274.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
             "https://images.pexels.com/photos/583842/pexels-photo-583842.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
             "https://images.pexels.com/photos/1327430/pexels-photo-1327430.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
             "https://images.pexels.com/photos/6686442/pexels-photo-6686442.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
             "https://images.pexels.com/photos/7586689/pexels-photo-7586689.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
             "https://images.pexels.com/photos/3916058/pexels-photo-3916058.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
             "https://images.pexels.com/photos/144428/pexels-photo-144428.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
             "https://i.pinimg.com/736x/db/6e/25/db6e25067820d52d69fcbe45c3725e57.jpg",
             "https://i.pinimg.com/564x/28/48/79/2848799ee345fbfa150333238819871b.jpg",
             "https://i.pinimg.com/750x/10/dc/ed/10dced43d153aa640abc90d30fb0463c.jpg",
             "https://i.pinimg.com/564x/90/fb/f6/90fbf6181ed4594ac92e634366b3b25d.jpg",
             "https://i.pinimg.com/564x/8d/1f/5e/8d1f5ed077cdb2d332db80074e2b728e.jpg",
             "https://i.pinimg.com/564x/50/76/77/5076772787507648973be6dc5b4cab0a.jpg",
             "https://i.pinimg.com/736x/53/44/e6/5344e6d3b2b63cbd2bd545681520637a.jpg",
             "https://i.pinimg.com/564x/00/2d/15/002d153ff13f17df77d20f551f453fa4.jpg",
             "https://i.pinimg.com/736x/5e/6c/6d/5e6c6dc989fb0c1815df8401d227a569.jpg",
             "https://i.pinimg.com/564x/df/66/ba/df66baf07afd6c6489bbd740ed91bcaf.jpg",
             "https://i.pinimg.com/564x/70/0b/46/700b4667cc8ca2aab13c9e203db636cb.jpg",
             "https://i.pinimg.com/564x/20/d4/5f/20d45fdddb3b71206242d1012b899370.jpg",
             "https://i.pinimg.com/564x/dd/85/49/dd8549d7e9f9a3541042e53ed7aeb64f.jpg",
             "https://i.pinimg.com/564x/35/7d/6e/357d6eaae91fb6277854ef160f8f0a24.jpg",
             "https://i.pinimg.com/564x/fd/a6/f0/fda6f04638c47e6fe0eef779f8548581.jpg",
             "https://i.pinimg.com/564x/12/25/69/12256922c6763fedc9ed81aeedeac7cb.jpg",
             "https://i.pinimg.com/564x/07/5d/8d/075d8d3cef7749e32360de9e74bb220d.jpg",
             "https://i.pinimg.com/564x/7c/81/9a/7c819a8746963db5ddc287adc4d12d6a.jpg",
             "https://i.pinimg.com/564x/26/95/1c/26951cfa2e9a8dc6cef1072f66df33ef.jpg",
             "https://i.pinimg.com/564x/e1/72/7a/e1727aa5692b952fa5a86e8930bb320a.jpg",
             "https://i.pinimg.com/736x/e0/ba/78/e0ba78e70423d60874f19189ec824065.jpg",
             "https://i.pinimg.com/564x/07/df/1b/07df1b69ed694fab05cf1b950b3855b9.jpg",
             "https://i.pinimg.com/564x/bd/42/44/bd4244030a28ef6ed89fd959e085d5ea.jpg",
             "https://i.pinimg.com/736x/f7/af/bd/f7afbd4d82ca2be18dfc3fea8c803490.jpg",
             "https://i.pinimg.com/564x/d7/a8/8e/d7a88e7d4a3fcf81a8a416c58f11bb6e.jpg",
             "https://i.pinimg.com/736x/87/3c/d3/873cd3e1dcfdd30a4d6a9b91a2560205.jpg",
             "https://i.pinimg.com/564x/76/1b/3f/761b3f21fec8a951dbaedad0d8eb4474.jpg",
             "https://i.pinimg.com/736x/65/b1/9b/65b19b19b79c846a56a0eea951d227a9.jpg",
             "https://i.pinimg.com/736x/be/9f/8f/be9f8f8533d60a7625b75763d882ca65.jpg",
             "https://3.bp.blogspot.com/-aO22ry-6TUs/WzHQOvfAyFI/AAAAAAAA5a0/AeA8QpWjfyM2p5dP2SSmJROKBUoy0xnGwCLcBGAs/s400/34.jpg",
             "https://3.bp.blogspot.com/-sl9HRtsQLHI/WzHQRG_R0PI/AAAAAAAA5bg/l9_b3SW5dZk7O0zQBkEaNip9yUIshxxCQCLcBGAs/s640/44.jpg",
             "https://3.bp.blogspot.com/-S8yLg1Hipok/WzHQIxwW2xI/AAAAAAAA5ZI/XW5RSYXN5eE3lbC_JpQb6Tg19qYLGRAsQCLcBGAs/s400/11.png",
             "https://4.bp.blogspot.com/-1Q2oql3gnIA/WzHQOrCF84I/AAAAAAAA5as/haBtRwh3rWATd59T7ye_qtVigOA1q-RDgCLcBGAs/s320/33.jpg",
             "https://3.bp.blogspot.com/-DtMjSpe4fv8/WzHQOSCLUaI/AAAAAAAA5aw/9YnW1uWlWQI1Ozt3VoLTkrQbPytnIBs5wCLcBGAs/s640/32.jpg",
             "https://i.pinimg.com/564x/a6/14/96/a61496b3c06583e3ef80ae12885e9608.jpg",
             "https://i.pinimg.com/564x/13/ce/a3/13cea3a41e8fb9caa5fefbc198df2f12.jpg",
             "https://i.pinimg.com/236x/26/05/a7/2605a7636534754b25c72f932fdfae09.jpg",
             "https://i.pinimg.com/564x/89/9d/28/899d2827475613cb9035908857c57775.jpg",
             "https://i.pinimg.com/564x/ba/a4/b0/baa4b090a96c7994a32a7dfd7a46cb74.jpg",
             "https://i.pinimg.com/564x/1c/27/17/1c271720890bacd0c7872333f49a1191.jpg",
             "https://i.pinimg.com/564x/61/4d/6a/614d6a0ec49015f8cd9d21ef37f48f19.jpg",
             "https://i.pinimg.com/564x/f7/a2/8c/f7a28c10c294e64aa15a756f2ea6c845.jpg",
             "https://i.pinimg.com/736x/5c/7f/60/5c7f60d549730d4d862370eabc7d098d.jpg",
             "https://i.pinimg.com/564x/38/52/86/38528672dad7c1ea57b831107f71c595.jpg",
             "https://i.pinimg.com/564x/5f/3c/35/5f3c3574124558c849fc05fa36c60821.jpg",
             "https://i.pinimg.com/564x/85/b8/52/85b852fe429f4f17ed1bfd3a6de20a75.jpg",
             "https://i.pinimg.com/736x/95/df/69/95df691de03240628f573f73a7769a97.jpg",
             "https://i.pinimg.com/736x/7f/2e/82/7f2e829fe19b0c578a3bfac44acd2462.jpg",
             "https://i.pinimg.com/736x/4b/90/bc/4b90bc4be4a88440597389dcb68b5d93.jpg",
             "https://i.pinimg.com/564x/26/f8/62/26f862e873121b066500692d631f11b1.jpg",
             "https://i.pinimg.com/564x/82/25/a4/8225a4e907f557044da3df3791c94c5d.jpg",
             "https://i.pinimg.com/564x/a3/f6/58/a3f658a3575601e1a80fa9ae4b105dc5.jpg",
             "https://i.pinimg.com/564x/da/74/4a/da744af699e81b90ec1f9f3f2000a25e.jpg",
             "https://i.pinimg.com/736x/e5/0b/e5/e50be507c9e497aeeaa0217d4d56ac73.jpg",
             "https://i.pinimg.com/564x/2e/9c/93/2e9c93f7df75483df06f3685f145e92d.jpg",
             "https://i.pinimg.com/564x/c4/74/70/c474708849903314bf26edee08db6265.jpg",
             "https://i.pinimg.com/564x/f3/63/e9/f363e969faf6cd5fb5848d3b43697870.jpg",
             "https://i.pinimg.com/564x/3f/1e/6d/3f1e6d5258e56dfb79283701cba5a665.jpg",
             "https://i.pinimg.com/564x/0c/6a/78/0c6a788a868ad6793bbc56c9a4e1b59b.jpg",
             "https://i.pinimg.com/564x/ca/2a/d6/ca2ad636313c30280b340bbe9670b5eb.jpg",
             "https://i.pinimg.com/564x/43/c2/9f/43c29f815225ad2f3dc4c1372a92d7df.jpg",
             "https://i.pinimg.com/564x/54/1b/09/541b0967df0ce05ed6b198f563d30d92.jpg",
             "https://i.pinimg.com/564x/f3/2a/b2/f32ab2065a91a84369592cd3778608d9.jpg",
             "https://i.pinimg.com/736x/05/60/0a/05600a6dc19a37ef746fb267902398bf.jpg",
             "https://i.pinimg.com/736x/61/82/e4/6182e4b0df653cda08509083e134b6b4.jpg",
             "https://i.pinimg.com/564x/3d/2f/f1/3d2ff1c862061f3bb9121d1040939cb4.jpg",
             "https://i.pinimg.com/736x/92/84/86/92848671a09b93e5e8fc09c480d78303.jpg",
             "https://i.pinimg.com/564x/ab/f1/44/abf1445201a140fb9527941e0f71e65b.jpg",
             "https://i.pinimg.com/564x/a8/8d/3a/a88d3a5862701f75497a7244c0cfb231.jpg",
             "https://i.pinimg.com/736x/82/3e/4a/823e4a3ee93ac4915c0e6a2dc7da840c.jpg",
             "https://i.pinimg.com/564x/47/21/70/4721701d072e38116f9e10308c019f46.jpg",
             "https://i.pinimg.com/736x/0f/fd/db/0ffddb9c11bae43238c02aa6743ce4be.jpg",
             "https://i.pinimg.com/736x/c9/31/26/c931266736fd0154c5e89fa63323c7fb.jpg",
             "https://i.pinimg.com/564x/48/c0/58/48c05843daf1959abbdcf4dd013324bf.jpg",
             "https://i.pinimg.com/564x/6e/4a/cf/6e4acfab3ec6d56d973d521517f006a8.jpg",
             "https://i.pinimg.com/736x/47/bc/29/47bc29e0a53854c68370c94654a2abc0.jpg",
             "https://i.pinimg.com/736x/14/2a/3e/142a3e5775a0dfc4e8a252cf409d107b.jpg",
             "https://i.pinimg.com/736x/46/fe/d2/46fed2d1abd80f4a0c3bacabb06895ed.jpg",
             "https://i.pinimg.com/736x/78/e2/60/78e260cc327464365ed960e0a5ab4a08.jpg",
             "https://i.pinimg.com/736x/e7/0c/48/e70c489c323ffd2a4d6b91f248ea3679.jpg",
             "https://i.pinimg.com/564x/30/2a/f0/302af0425b4ceec1aaf617f5f1bef94b.jpg",
             "https://i.pinimg.com/736x/e5/cb/f0/e5cbf000b7a10b9bd096e3f86fd61f21.jpg",
             "https://i.pinimg.com/564x/5a/ef/26/5aef26836d6af1a8b4911dc72b9d9a3b.jpg",
             "https://i.pinimg.com/564x/c4/ce/6c/c4ce6c9618449eab48305e29cef30949.jpg",
             "https://i.pinimg.com/564x/02/b8/8b/02b88ba3815cf27507a050efec18d177.jpg",
             "https://i.pinimg.com/564x/30/77/4f/30774f1428dc68d621b8d4cbe0ae2f51.jpg",
             "https://i.pinimg.com/736x/cf/d0/22/cfd02285a19982a053780cac8dfc49a5.jpg",
             "https://i.pinimg.com/564x/35/0f/fb/350ffb26403c4e4cee9417b61e906d16.jpg",
             "https://i.pinimg.com/736x/3d/c1/b9/3dc1b9ab16f999e8177b1a6a934254ca.jpg",
             "https://i.pinimg.com/750x/ff/94/77/ff947782e5022c5f88a1b45dcd11791a.jpg",
             "https://i.pinimg.com/736x/e3/18/b1/e318b105db511080c5a5df2f29e73c6e.jpg",
             "https://i.pinimg.com/736x/98/f0/c7/98f0c7b91b6ec95cf5b2cee78e004959.jpg",
             "https://i.pinimg.com/736x/ff/e2/10/ffe210f0f195d9775e3606d1cc331a62.jpg"
             ]
boom = randint(0, len(backup_imgs))

###### get name of song track and fetch url of img ####
def get_cover_art(artist_name,next_name):
    print(artist_name,"received",next_name)

    artist_info = requests.get(
        'https://api.spotify.com/v1/search',
        headers=headers,
        params={'q': artist_name, 'type': 'track'})
    print("STATUS:", artist_info.status_code)
    print("CONTENT TYPE:", artist_info.headers.get("Content-Type"))
    print("TEXT:", artist_info.text[:500])
    print("URL:", artist_info.url)
    print("BODY:", artist_info.text)
    data = artist_info.json()
    try:
        uri_p = data["tracks"]["items"][0]["album"]["images"][0]["url"]
        print('this is ',artist_name,next_name)
        return uri_p,artist_name.title(),next_name[:-4].title()
    except Exception as e:
        print(e,'ugh',data)
        print(traceback.format_exc(),'whatever')
        # or
        print(sys.exc_info()[2],'wth')
        print('working here',next_name)
        return backup_imgs[boom],artist_name.title(),next_name[:-4].title()
