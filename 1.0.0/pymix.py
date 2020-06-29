import pygame
import random
import time

from os import listdir
from os.path import isfile, join


class Pymix:

    def __init__(self,p_vol,pathcalm='musicologie/musiques/Calm/',pathanger='musicologie/musiques/Action/',pathsad='musicologie/musiques/Sad/'):
        """The builder of the 'Pymix' class

        Class for creating real time soundtrack.
        It launchs pygame mixer, stores all the file in list store in the tuple a_soundfile
        and a_label is used to labelize our four emotions.

        """
        pygame.mixer.init()
        self.a_vol = p_vol
        self.a_path = [pathcalm,pathanger,pathsad]
        self.a_soundfile = (self.get_file(pathcalm),self.get_file(pathanger),self.get_file(pathsad))
        self.a_label = {'calm':0,'anger':1,'sad':3}
        self.a_sound = None
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
        music = pygame.mixer.Sound(file)
        music.set_volume(self.a_vol)
        channel.play(music, fade_ms=fade_in)
        return 1

    def add_track_from_directory(self,pathdirectory,channel=7,fade_in=3000):
        """

        """
        listfile = self.get_file(pathdirectory)
        sound = pathdirectory + random.choice(listfile)
        play = pygame.mixer.Sound( sound )
        play.set_volume(self.a_vol)
        pygame.mixer.Channel(channel).play( play,fade_ms=fade_in )

    def add_feeling(self,feeling,fade_in=3000,rand=True,file=None):
        """
        Add a track linked to an emotion and play it in his personnal channel.
        The file is choosen randomly in the list of it emotion if rand is True, otherwise the file
        has to be specified in the file arg.
        """
        if type(feeling)==str : channel = self.a_label[feeling]
        else : channel = feeling
        if rand:
            self.a_sound = self.a_path[channel]+random.choice(self.a_soundfile[channel])
            print(self.a_sound)
            son = pygame.mixer.Sound( self.a_sound )
            son.set_volume(self.a_vol)
            pygame.mixer.Channel(channel).play(son ,fade_ms=fade_in )
            
        else:
            pygame.mixer.Channel(channel).play( pygame.mixer.Sound(file),fade_ms=fade_in )
        return 1

    def kill_feeling(self,feeling,fade_out=3000):
        """Stop a track related to the feeling gave in parameters."""
        if type(feeling)==str : channel = self.a_label[feeling]
        else : channel = feeling
        pygame.mixer.Channel(channel).fadeout(fade_out)
        return 1

    # def set_volume(self,vol, channel=None):
    #     if channel:
    #         pygame.mixer.Channel(channel).set_volume(vol)
    #         return
    #     pygame.mixer.music.set_volume(vol)
    #     return

    def get_volume(self,channel=None):
        if channel: return pygame.mixer.Channel(channel).get_volume()
        return pygame.mixer.music.get_volume()

    def pause_feeling(self,feeling,fade_out=3000):
        pass

    def play_feeling(self,feeling,duration=3):
        pass

    def get_feeling_busy(self):
        return [pygame.mixer.Channel(0).get_busy(),
                pygame.mixer.Channel(1).get_busy(),
                pygame.mixer.Channel(2).get_busy(),
                pygame.mixer.Channel(3).get_busy()]

    def state(self):
        li = self.get_feeling_busy()
        return li.index(max(li))

