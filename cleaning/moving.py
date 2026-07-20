import os
import shutil

import os
dir_path = os.path.dirname("D:\Aishu's Happiness")
songs=[]
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            # print(root + '\\' + str(file))
            songs.append(root + '\\' + str(file))

for song in songs:
  name=song.replace("D:\Aishu's Happiness\\",'')
  try:
    os.rename(song, "D:\Aishu's Happiness\My Music List\\"+name)
    os.replace(song, "D:\Aishu's Happiness\My Music List\\"+name)
    shutil.move(song, "D:\Aishu's Happiness\My Music List\\"+name)
  except:
    pass
  print(name)