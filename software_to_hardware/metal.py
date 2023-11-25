import sounddevice as sd
import numpy as np
import time
# import soundfile as sf
# pip install sounddevice


def get_decibels(dev):

    #how long i want to record for in sec:
    duration = 5

    #samples/sec
    rate = 44100 #HZ?

    chunk_size = int(duration*rate)
    #chunk_size = 1024


    #capture audio
    audio_rec = sd.rec(chunk_size, samplerate = rate, channels = 1, dtype = np.int16, device = dev)
    sd.wait()

    if not audio_rec.any():
        print("Empty data. Skipping calculation.")
        

    #RMS - getting root mean quare of audio signal: 
    rms = np.sqrt(np.mean(np.square(np.abs(audio_rec))))

    if rms <= 0:
        print("Invalid RMS value. Skipping calculation.")



    #convert RMS to decibels: 
    results = 20 * np.log10(rms)

    time.sleep(1)

    return results


#/////////////
# mic is where it's getting the audio from; usually 1 but not always guaranteed to be constant. // needs testing
mic = 0
decibels = get_decibels(mic)




# for testing
if decibels > 60:
    print(decibels)
    print("yawr")

else:
    print(decibels)
    print("nawr")




