import io
import pyqrcode
import eel
from pygame import mixer
import moviepy.editor as mp
import os
from mutagen.mp3 import MP3
from cover_art import get_cover_art
from random import choice,shuffle
from threading import Event, Thread
from time import sleep
curr=''
fine = True
eel.init('web')
pausev=True
first=True
start = False
order=[]
check=0
passthro=5
looop=1
gem=''
def ensure_mixer():
    try:
        mixer.music.get_busy()
    except Exception as e:
        print('mixer seems dead, reinitializing:', e)
        try:
            mixer.quit()
        except Exception:
            pass
        mixer.pre_init(44100, 16, 2, 4096)
        mixer.init()
@eel.expose
def generate_qr(data):
    global check, start,first,count,looop
    ensure_mixer()
    print('data value is',data)
    if data == 0:
        if looop == 0:
            looop = 1
            print('changing loop to 1')
        else:
            looop = 0
            print('changing loop to 0')


        print('loooping!!!')
    if first:
        check=0
        first=False
    if not first and data==1:
        print('calling play fn')
        play()
        start=True

    if data==3:
        print('calling play fn')
        if not looop:
            count+=1
            print(looop,'so and so',count)
            play(skip=True)
        else:
            play(skip=True)
            print(looop,'so and else',count)

        start = False
    # elif data==2:
    #     print('calling pause babygirl')
    #     pause(check)
    #     check+=1
    elif data==2:
        print('calling pause babygirl')
        if mixer.music.get_busy() and not mixer.music.get_pos() == -1:
            pause(0)  # force pause
        else:
            pause(1)  # force play
    if data==7:
        # looping same
        global curr,order
        shuffle(order)
        count=0
        print('order changed to',order)
        # play(True)

        # if looop%2!=0:
        #     print('ah-oh',curr)
        #
        #     mixer.music.rewind()
        #     mixer.music.queue(curr)
        #     looop+=1
        # else:
        #     mixer.music.queue(curr).pop()





        pass
    if data==9:
        if not looop:
            count-=1
            print(looop,'so and so',count)
            play(True)
        else:
            play(True)
            print(looop,'so and else',count)

        # else:
        #     count-=1
        print('now count is ',count)
        # play(True)
    # if data==3 or data==1:
    #     if not looop:
    #         count+=1
    #         print(looop,'so and so',count)
    #         play(True)
    #     else:
    #         play()
    #         print(looop,'so and else',count)
    #
    #     img=pyqrcode.create(data)
    #     buffers = io.BytesIO()
    #     img.png(buffers, scale=8)
        # encoded = b64encode(buffers.getvalue()).decode("ascii")
        # print("QR code generation successful.")

    if looop==0:
        # count-=1
        print('terrible logic',looop,count)

    global gem
    print(order[(count+1)%len(order)],'order')
    # print(get_cover_art(gem[:-4]),order[count+1])
    return get_cover_art(gem[:-4],order[(count+1)%len(order)])
# from pathlib import Path

# music_file = str(Path(__file__).parent / "MagicMusicSongs")
# Path(music_file).mkdir(parents=True, exist_ok=True)
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    # Running as a packaged .exe/.app
    app_dir = Path(sys.executable).parent
else:
    # Running as a normal .py script
    app_dir = Path(__file__).parent

music_file = str(app_dir / "MagicMusicSongs")
Path(music_file).mkdir(parents=True, exist_ok=True)
# music_file="D:\Aishu's Happiness\My Music List"
# music_file="D:\debug-videos"
fileDir = music_file
fileExt = r".mp3"

looop=0
order=[_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
shuffle(order)
global count
count=0
print(order,'the brand new confusion')
def convert(which):
    my_clip = mp.VideoFileClip(which)
    my_clip.audio.write_audiofile(f"{which[:-4]}.mp3")
    return f"{which[:-4]}.mp3"

def play(skip=False):
    global start,passthro,curr,fine,gem,count,looop
    ensure_mixer()
    fine = False
    # print('count before positive',count)
    # if count<0:
    #     count*=-1
    # print('count after positive',count)
    count%=len(order)
    print('count after mod',count)
    print('start',start)
    if skip:
            print('works')
            # gem = choice(os.listdir(music_file))
            # gem = choice(order)
            gem = order[count]
            # if looop==0:
            #     count+=1
            print('count was',count,'hence song ',gem,looop)
            while "AlbumArt" in gem or "Folder" in gem:
                # gem = choice(os.listdir(music_file))
                gem = order[count]

            print(gem)
            query_string = 'https://www.google.com/search?tbm=isch&q=' + gem
            print('no issue babyyyyyyy')
            # if gem:
            #     mixer.pre_init(44100, 16, 2, 4096)
            #     mixer.init()
            #     print(music_file + "\\" + gem)
            #     print(music_file + "\\" + gem[:-4] + '.mp3')
            #     try:
            #         mixer.music.load(music_file + "\\" + gem[:-4] + '.mp3')
            #         try:
            #             a = mixer.Sound(music_file + "\\" + gem[:-4] + '.mp3')
            #         except:
            #             sleep(0.5)
            #             a = mixer.Sound(music_file + "\\" + gem[:-4] + '.mp3')

            #         curr=music_file + "\\" + gem[:-4] + '.mp3'
            #         print("length", a.get_length())
            #         print('curr',curr)

            #         passthro = a.get_length()
            #     except:
            #         diamond = convert(music_file + "\\" + gem)
            #         mixer.music.load(diamond)
            #         a = mixer.Sound(diamond)
            #         curr=diamond
            #         print("length", a.get_length())

            #         passthro=a.get_length()
            #     print('am gonna sing lalalaaaa')
            #     if pausev:
            #         mixer.music.play()
            #     return get_cover_art(gem[:-4],order[(count+1)%len(order)])
            if gem:
                mixer.pre_init(44100, 16, 2, 4096)
                mixer.init()
                print(os.path.join(music_file, gem))
                print(os.path.join(music_file, gem[:-4] + '.mp3'))
                try:
                    mixer.music.load(os.path.join(music_file, gem[:-4] + '.mp3'))
                    try:
                        a = mixer.Sound(os.path.join(music_file, gem[:-4] + '.mp3'))
                    except:
                        sleep(0.5)
                        a = mixer.Sound(os.path.join(music_file, gem[:-4] + '.mp3'))

                    curr = os.path.join(music_file, gem[:-4] + '.mp3')
                    print("length", a.get_length())
                    print('curr', curr)

                    passthro = a.get_length()
                except:
                    diamond = convert(os.path.join(music_file, gem))
                    mixer.music.load(diamond)
                    a = mixer.Sound(diamond)
                    curr = diamond
                    print("length", a.get_length())

                    passthro = a.get_length()
                print('am gonna sing lalalaaaa')
                if pausev:
                    mixer.music.play()
                return get_cover_art(gem[:-4], order[(count + 1) % len(order)])
            start=False
    print('crucial',start)

    while not mixer.music.get_busy() and not start:

            print('works')
            # gem=choice(os.listdir(music_file))
            gem = order[count]
            # if looop%2!=0:
            #     count+=1
            print('count is',count,'hence song ',gem,looop)

            while "AlbumArt" in gem or "Folder" in gem:
                gem = choice(os.listdir(music_file))

            print(gem)
            query_string = 'https://www.google.com/search?tbm=isch&q='+gem
            print('no issue babyyyyyyy')
            if gem:
                    mixer.init()
                    # print(music_file+"\\"+gem)
                    print(os.path.join(music_file, gem))
                    # print(music_file+"\\"+gem[:-4]+'.mp3')
                    print(os.path.join(music_file, gem[:-4] + '.mp3'))
                    try:
                        # mixer.music.load(music_file+"\\"+gem[:-4]+'.mp3')
                        mixer.music.load(os.path.join(music_file, gem[:-4] + '.mp3'))
                        # a =  MP3(music_file+"\\"+gem[:-4]+'.mp3')
                        a =  MP3(os.path.join(music_file, gem[:-4] + '.mp3'))
                        print("length", a.info.length)
                    except:
                        # diamond=convert(music_file+"\\"+gem)
                        diamond=convert(os.path.join(music_file, gem))
                        mixer.music.load(diamond)
                        a =  MP3(diamond)
                        print("length", a.info.length)
                    print('am gonna sing lalalaaaa',gem)

                    mixer.music.play()
                    print("getting cover now")
                    return get_cover_art(gem[:-4],order[(count+1)%len(order)])

                    # mixer.music.set_volume(0.5)

def pause(check):
    ensure_mixer()
    print(check,'so')
    global start,first,pausev,fine
    if check%2==0:
        mixer.music.pause()
        start=True
        pausev=False
        first=False
        print('pausing')
    else:
        mixer.music.unpause()
        start=False
        first=True
        pausev=True
        fine = False
        print('time to play')

def stop():
    mixer.music.stop()
print(start)
print('bug',first)
while not first:
    print('okayish')
    play()
print('detect',start)

def my_update():
    global start,pausev,fine,count
    start=False
    print('#',pausev,'f',fine,start)
    if pausev and not fine:
        sleep(5)
        if not start and not mixer.music.get_busy():
            print('taking extra care',fine,start)
            print("booom")
            eel.fine1()
            if not looop:
                count+=1
            play()
            print('new song up')
        else:
            print('old playing still')
    else:
        print('strictly paused')


def call_repeatedly(interval, func, *args):
    interval = passthro
    stopped = Event()
    def loop():
        print('let us see', interval)

        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()
    return stopped.set

call_repeatedly(passthro, my_update)


# cancel_future_calls = call_repeatedly(5, print, "Hello, World")
# if not mixer.music.get_busy():
#
#     cancel_future_calls()


        # play()
@eel.expose
def adjustVol(how_much):
    ensure_mixer()
    how_much=int(how_much)
    mixer.music.set_volume(how_much/100)
    print('volume adjusted to ',how_much/100)
adjustVol(15)
eel.start('index.html', size=(1000, 600))
