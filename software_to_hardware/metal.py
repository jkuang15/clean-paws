import sounddevice as sd
import numpy as np
import soundfile as sf
# pip install sounddevice
def db(data):
    rms = np.sqrt(np.mean(data**2))
    reference = 1.0 #based on mic sensitivity
    decibel_level = 20* np.log(rms/reference)
    return decibel_level

#settings
duration = 5
sample_rate = 44100 #HZ?
filename = "recording.wav"

#capture audio
audio_record = sd.rec(int(duration * sample_rate), sample_rate = sample_rate, channels = 1, dtype =  'int16')

#saving to WAV file

sf.write(filename, audio_record, sample_rate)

#calculate decibel level
decibel_level = db(audio_record)



if 0 < decibel_level < 10:
    print("no")

else:
    print("yAwr")