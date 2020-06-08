#importation du module qui permet le record du son
import pyaudio
#import pour la creation de .wav
import wave
import time
#Décommenter cette ligne pour plt les graphiques
import matplotlib.pyplot as plt
import numpy
import soundfile as sf

class Recorder(object):


    def __init__(self, channels=1, rate=44100, frames_per_buffer=1024):
        self.a_channels = channels
        self.a_rate = rate
        self.a_frames_per_buffer = frames_per_buffer

    def open(self, fname, mode='wb'):
        return RecordingFile(fname, mode, self.a_channels, self.a_rate,
                            self.a_frames_per_buffer)

class RecordingFile(object):
    """ Création de la classe RecordingFile. Cette classe permet l'enregistrement du microphone pendant  secondes.
    L'enregistrement peut etre lancer avec la fonction start_recording() puis enregistré avec la fonction write_on_file()
    """
    def __init__(self, fname, mode, channels, 
                rate, frames_per_buffer):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None
        self.abs_data = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def amplitude(self,plot):
        data, samplerate = sf.read(self.fname)
        self.abs_data = abs(data)

        if(plot):
            #décommenter la section ci-dessous pour voir les graphiquesS
            plt.plot(self.abs_data)
            plt.ylabel('Amplitude')
            plt.show()
            
        return self.abs_data

    def moyenne(self):
        return numpy.mean(self.abs_data)

    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile


GetS = Recorder()
S = GetS.open('Sortie_GetS.wav')
S.start_recording()
print("Lancement du son")
time.sleep(5)
print("hop hop on stop le record")
S.stop_recording()
print(S.amplitude(plot = True))

print(S.moyenne())
