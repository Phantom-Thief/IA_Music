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
        self.a_label = {'joy':0,'anger':1,'calm':2,'sad':3}
        pygame.mixer.set_num_channels(8)
        pygame.mixer.set_reserved(0)
        pygame.mixer.set_reserved(1)
        pygame.mixer.set_reserved(2)
        pygame.mixer.set_reserved(3)

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

    def add_track(self,file,channel=7,fade_in=3000):
        """Play an audio file in the specified channel."""
        if channel < 5 : print("Warning : channel {} already used for feelings".format(channel))
        channel = pygame.mixer.Channel(channel)
        channel.play(pygame.mixer.Sound(file),fade_ms=fade_in)
        return 1

    def add_feeling(self,feeling,fade_in=3000,rand=True,file=None):
        """
        Add a track linked to an emotion and play it in his personnal channel.
        The file is choosen randomly in the list of it emotion if rand is True, otherwise the file
        has to be specified in the file arg.
        """
        if type(feeling)==str : channel = self.a_label[feeling]
        else : channel = feeling
        if rand:
            sound = self.a_path[channel]+random.choice(self.a_soundfile[channel])
            print(sound)
            pygame.mixer.Channel(channel).play( pygame.mixer.Sound( sound ),fade_ms=fade_in )
        else:
            pygame.mixer.Channel(channel).play( pygame.mixer.Sound(file),fade_ms=fade_in )
        return 1

    def kill_feeling(self,feeling,fade_out=3000):
        """Stop a track related to the feeling gave in parameters."""
        if type(feeling)==str : channel = self.a_label[feeling]
        else : channel = feeling
        pygame.mixer.Channel(channel).fadeout(fade_out)
        return 1

    def get_feeling_busy(self):
        return [pygame.mixer.Channel(0).get_busy(),
                pygame.mixer.Channel(1).get_busy(),
                pygame.mixer.Channel(2).get_busy(),
                pygame.mixer.Channel(3).get_busy()]

    def state(self):
        li = self.get_feeling_busy()
        return li.index(max(li))



# py = Pymix()
# py.add_feeling('calm')
# py.add_feeling('anger',fade_in=3000)
# print(py.get_all_busy())

# time.sleep(5)

# py.kill_feeling('calm')
# time.sleep(4)
# print(py.get_all_busy())
# print(py.state())
# time.sleep(1)