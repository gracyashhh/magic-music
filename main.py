from playsound import playsound

# import subprocess
video_input_path = "D:/Aishu's Happiness/jillu.mp4"
img_output_path = 'F:\\Projects-of-all-time\\Music-player\\Thumbnails'
# subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:00.000', '-vframes', '1', img_output_path])
from pyffmpeg import FFmpeg
# playsound(video_input_path)
# inf = video_input_path
# outf = img_output_path
#
# ff = FFmpeg()
# ff.convert(inf, outf)
import requests
import ffmpeg
import sys
from thumb_gen.worker import Generator

#video_path, output_path='', custom_text=True, font_dir='', font_size=
# app = Generator(video_input_path, img_output_path)
# app.run()
import moviepy.editor as mp
my_clip = mp.VideoFileClip(video_input_path)
# my_clip.audio.write_audiofile(r"my_result.mp3")
playsound(r"my_result.mp3")
