from io import BytesIO

import requests
import simpleaudio

response = requests.get("https://www2.cs.uic.edu/~i101/SoundFiles/CantinaBand3.wav")

audio_stream = BytesIO()
audio_stream.write(response.content)
audio_stream.seek(0)

wave_obj = simpleaudio.WaveObject.from_wave_file(audio_stream)
wave_obj.sample_rate = 44000  # TODO: set this appropriately
play_obj = wave_obj.play()  # start playing audio from bytes IO
play_obj.wait_done()