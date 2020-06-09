"""
All imports to be able to launch the program
import of the module that allows the sound record 'pyaudio'
import for the creation of .wav 'wave'
importation pour plot (format de test) 'matplotlib.pyplot as plt'
import for sound processing 'soundfile as sf'
"""
import pyaudio
import wave
import time
import _portaudio as pa
import matplotlib.pyplot as plt
import numpy
import soundfile as sf

class Recorder(object):
    """Creating the Recorder class. This class opens a .wav file that will store the recorded sound file.
    """
    def __init__(self, p_channels=1, p_rate=44100, p_frames_per_buffer=1024):
        self.a_channels=p_channels
        self.a_rate=p_rate
        self.a_frames_per_buffer=p_frames_per_buffer

    def open(self, p_fname, mode='wb'):
        return RecordingFile(p_fname, mode, self.a_channels, self.a_rate,
                            self.a_frames_per_buffer)

class RecordingFile(object):
    """ Creation of the RecordingFile class. This class allows the recording of the microphone during seconds.
    The recording can be started with the function start_recording() and then recorded with the function write_on_file().
    """
    def __init__(self, p_fname, p_mode, p_channels, 
                p_rate, p_frames_per_buffer):
        self.a_fname = p_fname
        self.a_mode = p_mode
        self.a_channels = p_channels
        self.a_rate = p_rate
        self.a_frames_per_buffer = p_frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.a_wavefile = self._prepare_file(self.a_fname, self.a_mode)
        self._stream = None
        self.a_abs_data = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()
    
    """
    start_recording' is used to start recording.
    Use a stream with a callback in non-blocking mode
    """
    def start_recording(self):
        
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.a_channels,
                                        rate=self.a_rate,
                                        input=True,
                                        frames_per_buffer=self.a_frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    """
    arrête l'enregistrement
    """
    def stop_recording(self):
        self._stream.stop_stream()
        return self


    """
    callback' is a function that allows you to launch our program in non-blocking mode.
    """
    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.a_wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    """
    function that calculates the amplitudes of the sound placed in input, calculates the amplitudes
    """
    def amplitude(self,p_plot=False):
        data, samplerate = sf.read(self.a_fname)
        self.a_abs_data = abs(data)

        if(p_plot):
            plt.plot(self.a_abs_data)
            plt.ylabel('Amplitude')
            plt.show()
            
        return self.a_abs_data

    """
    return the average of the calculated amplitudes
    """
    def moyenne(self):
        return numpy.mean(self.a_abs_data)

    """
    return
    """
    def extremum(self):
        return self.a_abs_data.max()
    

    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.a_wavefile.close()

    def _prepare_file(self, p_fname, mode='wb'):
        wavefile = wave.open(p_fname, mode)
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
