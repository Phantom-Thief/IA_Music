import Request_Api as api
import pymix
import time
import pygame



sound = pymix.Pymix()

path = 'D:/Projet_E3/IA_Music/musicologie/musiques/Action/1.Smash It Up-Main.wav' 

import pygame
import threading
import time


def play(sound, start, end):
    sound.set_pos(start)
    sound.play()
    time.sleep(end - start)     # in seconds
    sound.stop()
    return True



pygame.mixer.init()
sound = pygame.mixer.music.load(path)
pygame.mixer.music.play(start=0.5)

time.sleep(10)
while(pygame.mixer.get_busy()):
    pass
print("Finished")