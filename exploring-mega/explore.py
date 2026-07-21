from mega import Mega
import json
import os
from dotenv import load_dotenv
load_dotenv()
mega = Mega()
email=os.getenv('mega_email')
password=os.getenv('mega_password')
# email=""
# password=""
m = mega.login(email, password)
# # login using a temporary anonymous account

details = m.get_user()

quota = m.get_quota()
# specify unit output kilo, mega, gig, else bytes will output
space = m.get_storage_space(giga=True)
files = m.get_files()

print("user details: ",details)
print("Quota: ",quota)
print("Space left: ",space)
print("Files in here: ",files)
json_string = json.dumps(files, indent = 6)
print(json_string)
file = m.find('magaley.mp3')
print(file)
try:
    m.download(file,'F:\Projects-of-all-time\Music-player\exploring-mega')
except:
    pass
print('success bby')
# from mega import Mega
# import tempfile
#
# # Login to mega
# mega = Mega()
# email="aishwaryam.campk12@gmail.com"
# password="testapp123"
# m = mega.login(email, password)

# # Get the file descriptor of a previously uploaded file
# filename='file_example_MP3_700KB.mp3'
# filedesc = m.find(filename)
#
# with tempfile.TemporaryDirectory() as tmpdir:
#     # Download the file to a temporary directory
#     downloaded_file_name = m.download(filedesc, tmpdir)
#     # replace the following with pygame code for playing the downloaded_file_name file
#     print(downloaded_file_name)