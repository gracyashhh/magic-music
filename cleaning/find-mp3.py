import os
dir_path = os.path.dirname("D:\Aishu's Happiness")
songs=[]
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            print(root + '\\' + str(file))
            songs.append(root + '\\' + str(file))
