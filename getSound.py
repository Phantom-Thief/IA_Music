import pyaudio
import wave

class getSound:

    def init(self, chunk=1024, format=pyaudio.paInt16, channels=1, sample_rate=44100):
        self.a_record = None
        self.a_chunk=chunk
        self.a_format=format
        self.a_channels=channels
        self.a_sample_rate=sample_rate
        self.a_pyaudio = pyaudio.PyAudio()

    def write_on_file(self,filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.a_channels)
        wf.setsampwidth(self.a_pyaudio.get_sample_size(self.a_format))
        wf.setframerate(self.a_sample_rate)
        wf.writeframes(b''.join(self.a_record))
        wf.close()

    def record(self, duration):
        #fichier de sortie pour test
        #sortie_test = "output.wav"

        # initialize PyAudio object
        p = self.a_pyaudio
        # open stream object as input & output
        stream = p.open(format=self.a_format,
                        channels=self.a_channels,
                        rate=self.a_sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=self.a_chunk)
        frames = []
        print("Recording...")
        for i in range(int(44100 / self.a_chunk * duration)):
            data = stream.read(self.a_chunk)
            # if you want to hear your voice while recording
            # stream.write(data)
            frames.append(data)
        print("Finished recording.")
        self.a_record = frames
        # stop and close stream
        stream.stop_stream()
        stream.close()
        # terminate pyaudio object
        p.terminate()
