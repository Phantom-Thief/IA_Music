import pyaudio
import wave

class getSound:

    def init(self,a_duration):
        self.a_record = None
        self.duration = a_duration

    def record(self):
        # set the chunk size of 1024 samples
        chunk = 1024
        # sample format
        FORMAT = pyaudio.paInt16
        # mono, change to 2 if you want stereo
        channels = 1
        # 44100 samples per second
        sample_rate = 44100

        #fichier de sortie pour test
        #sortie_test = "output.wav"

        # initialize PyAudio object
        p = pyaudio.PyAudio()
        # open stream object as input & output
        stream = p.open(format=FORMAT,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)
        frames = []
        print("Recording...")
        for i in range(int(44100 / chunk * self.duration)):
            data = stream.read(chunk)
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

        #partie des tests
        # wf = wave.open(sortie_test, 'wb')
        # wf.setnchannels(channels)
        # wf.setsampwidth(p.get_sample_size(FORMAT))
        # wf.setframerate(sample_rate)
        # wf.writeframes(b''.join(frames))
        # wf.close()

sound = getSound(2)
sound.record()
#pour voir se que ça donne
#print("sortie audio : {}".format(sound.a_record))