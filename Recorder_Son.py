"""
Tous les imports pour pouvoir lancer le programme
"""
#importation du module qui permet le record du son
import pyaudio
#import pour la creation de .wav
import wave
import time
import _portaudio as pa
# cette ligne pour plt les graphiques
import matplotlib.pyplot as plt
import numpy
import soundfile as sf

class Recorder(object):
    """Création de la classe Recorder.
    """
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
        self.a_fname = fname
        self.a_mode = mode
        self.a_channels = channels
        self.a_rate = rate
        self.a_frames_per_buffer = frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.a_wavefile = self._prepare_file(self.a_fname, self.a_mode)
        self._stream = None
        self.a_abs_data = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.a_channels,
                                        rate=self.a_rate,
                                        input=True,
                                        frames_per_buffer=self.a_frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.a_wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def amplitude(self,plot=False):
        data = sf.read(self.a_fname)[0]
        self.a_abs_data = abs(data)

        if(plot):
            #décommenter la section ci-dessous pour voir les graphiques
            plt.plot(self.a_abs_data)
            plt.ylabel('Amplitude')
            plt.show()
            
        return self.a_abs_data

    def moyenne(self):
        return numpy.mean(self.a_abs_data)

    def extremum(self):
        return self.a_abs_data.max()
    

    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.a_wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.a_channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.a_rate)
        return wavefile


# GetS = Recorder()
# S = GetS.open('Sortie_GetS.wav')
# S.start_recording()
# print("Lancement du son")
# time.sleep(5)
# print("hop hop on stop le record")
# S.stop_recording()
# print(S.amplitude(plot = False))

# print(S.extremum())
