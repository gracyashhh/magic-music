from lyrics_extractor import SongLyrics
import os
from dotenv import load_dotenv

load_dotenv()

GCS_API_KEY = os.getenv('GCS_API_KEY')
GCS_ENGINE_ID = os.getenv('GCS_ENGINE_ID')
# works for hindi and english and some tamil songs
extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)
data = extract_lyrics.get_lyrics("veyyon silli")
print(data)

# <script async src="https://cse.google.com/cse.js?cx=f729e6d0eb349fc4e"></script>
# <div class="gcse-search"></div>
