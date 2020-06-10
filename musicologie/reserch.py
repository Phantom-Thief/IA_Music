import simpleaudio as sa
import numpy as np
import time
import wavio
import soundfile as sf
import winsound
import sounddevice as sd

time_start = time.time()
# wave_obj = sa.WaveObject.from_wave_file("exp.wav")
# play_obj = wave_obj.play()
# print("test")
# play_obj.wait_done()
# print("fini")

# tab = wavio.read("exp.wav") #ouverture objet wav
# print(tab.data.shape)
# tab.data = tab.data.mean(axis=1) # stéréo -> mono
# print(tab.data.shape)
# wavio.write("test.wav",tab.data,tab.rate,sampwidth=tab.sampwidth) #écriture nouveau fichier mono




# data1, fs1 = sf.read('exp.wav')
# data2, fs2 = sf.read('electro.wav')
# print("rate1 : {}, rate2 : {}".format(fs1,fs2))

# data1 = np.append(data1[:200000],data2[:20000])
# sd.play(data1, fs1+fs2)


# print("Programme terminé en {}".format(time.time()-time_start))
# sd.wait()

duration = 5.5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))