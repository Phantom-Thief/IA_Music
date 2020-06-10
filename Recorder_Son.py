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
    def __init__(self, p_channels=1, p_rate=44100, p_frames_per_buffer=1024):
        """The builder of the 'Recorder' class.

        This class opens a .wav file that will store the recorded sound file.

        """
        self.a_channels=p_channels
        self.a_rate=p_rate
        self.a_frames_per_buffer=p_frames_per_buffer

    def open(self, p_fname, mode='wb'):
        """Launch the 'RecordingFile'"""
        return RecordingFile(p_fname, mode, self.a_channels, self.a_rate,
                            self.a_frames_per_buffer)

class RecordingFile(object):
    def __init__(self, p_fname, p_mode, p_channels, 
                p_rate, p_frames_per_buffer):
        """ The builder of the 'RecordingFile' class.
        
        Creation of the RecordingFile class. This class allows the recording of the microphone during a given time.
        The recording can be started with the function start_recording() and then recorded with the function write_on_file().

        """
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
    
    def start_recording(self):
        """Use a stream with a callback in non-blocking mode, 'start_recording' is used to start the record."""
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.a_channels,
                                        rate=self.a_rate,
                                        input=True,
                                        frames_per_buffer=self.a_frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        """The 'stop_recording' function is used to stop the record."""
        self._stream.stop_stream()
        return self

    def get_callback(self):
        """callback' is a function that allows you to launch our program in non-blocking mode."""
        def callback(in_data, frame_count, time_info, status):
            self.a_wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback
    
    def amplitude(self,p_plot=False):
        """Return the amplitude of a .wav file.

        This function retrieves a .wav file and transforms it into a frequency.
        By calling this function with 'p_plot' = True, a graph is returned (attention blocking process).
        
        """
        data = sf.read(self.a_fname)[0]
        self.a_abs_data = abs(data)

        if(p_plot):
            plt.plot(self.a_abs_data)
            plt.ylabel('Amplitude')
            plt.show()
            
        return self.a_abs_data

    def moyenne(self):
        """Return the average of the calculated amplitudes."""
        return numpy.mean(self.a_abs_data)

    def extremum(self):
        """Return the maximum value in the list of amplitudes."""
        return self.a_abs_data.max()

    def close(self):
        """Shut everything down."""
        self._stream.close()
        self._pa.terminate()
        self.a_wavefile.close()

    def _prepare_file(self, p_fname, mode='wb'):
        """Create and open a .wav file that will store the requested record."""
        wavefile = wave.open(p_fname, mode)
        wavefile.setnchannels(self.a_channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.a_rate)
        return wavefile
