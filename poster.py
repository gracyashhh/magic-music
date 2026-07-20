from bs4 import BeautifulSoup
import pandas as pd
import requests
from time import sleep
from datetime import date, timedelta

# create empty arrays for data we're collecting
dates = []
url_list = []
final = []

# map site

url = "https://spotifycharts.com/regional/in/daily/"
start_date = date(2021, 1, 1)
end_date = date(2021, 10, 19)

delta = end_date - start_date

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    day_string = day.strftime("%Y-%m-%d")
    print(day_string)
    dates.append(day_string)

print(dates)

def add_url():
    for data in dates:
        c_string = url + data
        url_list.append(c_string)
    print(url_list)

add_url()


# function for going through each row in each url and finding relevant song info

def song_scrape(x):
    pg = x
    try:
        for tr in pg.find("tbody").findAll("tr"):

            artist = tr.find("td", {"class": "chart-table-track"}).find("span").text
            artist = artist.replace("by ", "").strip()
            print(artist)
            title = tr.find("td", {"class": "chart-table-track"}).find("strong").text
            print(title)
            songid = tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
            songid = songid.split("track/")[1]
            print(songid)
            songimg=tr.find("td", {"class": "chart-table-image"}).find("a").find("img").get("src")
            # print(songimg.img)
            print('ahem',songimg)


            final.append([title, artist, songid,songimg])
    except:
        print('justuuu miss uh')


# loop through urls to create array of all of our song info

for u in url_list:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    read_pg = requests.get(u,headers=headers)
    sleep(2)
    soup = BeautifulSoup(read_pg.text, "html.parser")
    songs = soup.find("table", {"class": "chart-table"})
    # print(songs)
    song_scrape(songs)


# convert to data frame with pandas for easier data manipulation

final_df = pd.DataFrame(final, columns=["Title", "Artist", "Song ID", "Image URL"])

# write to csv

with open('spmooddata.csv', 'w') as f:
    final_df.to_csv(f, header=True, index=False)