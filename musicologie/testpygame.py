import pygame
import time
import random
from os import listdir
from os.path import isfile, join


class Pymix:

    def __init__(self,pathjoy='musicologie/musiques/joyeux/',pathanger='musicologie/musiques/colere/',pathcalm='musicologie/musiques/calme/',pathsad='musicologie/musiques/triste/'):
        """The builder of the 'Pymix' class

        Class for creating real time soundtrack.
        It launchs pygame mixer, stores all the file in list store in the tuple a_soundfile
        and a_label is used to labelize our four emotions.

        """
        pygame.mixer.init()
        self.a_path = [pathjoy,pathanger,pathcalm,pathsad]
        self.a_soundfile = (self.get_file(pathjoy),self.get_file(pathanger),self.get_file(pathcalm),self.get_file(pathsad))
        self.a_label = {'joy':0,'anger':1,'calm':2,'sadness':3}

    def get_file(self,path):
        """Method used to have the list of all files in a directory."""
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles

    def is_busy(self):
        """Return True if pygame is currently playing music."""
        return pygame.mixer.get_busy()

    def stop(self):
        """Stop the pygame's mixer and all the sound."""
        pygame.mixer.stop()
        pygame.mixer.quit()

    def add_track(self,channel,file,fade_in=1000):
        """Play an audio file in the specified channel."""
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(file),fade_ms=fade_in)
        return 1

    def add_feeling(self,feeling,fade_in=1000,rand=True,file=None):
        """
        Add a track linked to an emotion and play it in his personnal channel.
        The file is choosen randomly in the list of it emotion if rand is True, otherwise the file
        has to be specified in the file arg.
        """
        channel = self.a_label[feeling]
        if rand:
            pygame.mixer.Channel(channel).play( pygame.mixer.Sound( self.a_path[channel]+random.choice(self.a_soundfile[channel]) ),fade_ms=fade_in )
        else:
            pygame.mixer.Channel(channel).play( pygame.mixer.Sound(file),fade_ms=fade_in )
        return 1

    def kill_feeling(self,feeling,fade_out=1000):
        """Stop a track related to the feeling gave in parameters."""
        channel = self.a_label[feeling]
        pygame.mixer.Channel(channel).fadeout(fade_out)
        return 1

    def get_all_busy(self):
        pass



py = Pymix()
py.add_feeling('calm')
time.sleep(10)
py.add_feeling('anger',fade_in=3000)
py.kill_feeling('calm',fade_out=3000)
input()