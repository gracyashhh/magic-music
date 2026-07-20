from lyrics_extractor import SongLyrics
GCS_API_KEY = 'AIzaSyAx9GBhdR_fDyM_wYzgYPGAQ-Brctn8c9c'
GCS_ENGINE_ID ='2d67307dfe87c6058'
# works for hindi and english and some tamil songs
extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)
data = extract_lyrics.get_lyrics("veyyon silli")
print(data)

# <script async src="https://cse.google.com/cse.js?cx=f729e6d0eb349fc4e"></script>
# <div class="gcse-search"></div>