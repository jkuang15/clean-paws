import sounddevice as sd
import numpy as np
import soundfile as sf
# pip install sounddevice


def get_decibels(dev):

    #how long i want to record for in sec:
    duration = 5

    #samples/sec
    rate = 44100 #HZ?

    chunk_size = int(duration*rate)


    #capture audio
    audio_rec = sd.rec(chunk_size, sample_rate = rate, channels = 1, dtype = np.int16, device = dev)
    sd.wait()

    #RMS - getting root mean quare of audio signal: 
    rms = np.sqrt(np.mean(np.square(audio_rec)))

    #convert RMS to decibels: 
    results = 20 * np.log(rms)

    return results


#/////////////
# mic is where it's getting the audio from; usually 1 but not always guaranteed to be constant. // needs testing
mic = 1
decibels = get_decibels(mic)




# for testing
if decibels > 60:
    print("yawr")

else:
    print("nawr")