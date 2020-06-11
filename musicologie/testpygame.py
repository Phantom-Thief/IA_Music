import pygame
import soundfile as sf
import time


# data, fs = sf.read("electro.wav")

# pygame.mixer.init()
# pygame.mixer.music.load('exp.wav')
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.Channel(0)
# pygame.mixer.music.play()
# input()
# pygame.mixer.Channel(1)
# pygame.mixer.music.play()
# input()
# pygame.mixer.music.stop()
# pygame.mixer.quit()


pygame.mixer.init()


pygame.mixer.Channel(0).play(pygame.mixer.Sound('exp.wav'),fade_ms=1000)
time.sleep(4)
pygame.mixer.Channel(1).play(pygame.mixer.Sound('exp.wav'))
time.sleep(1)
pygame.mixer.Channel(0).fadeout(1000)

# pygame.mixer.Channel(i+1).play(pygame.mixer.Sound('exp.wav'))


while(pygame.mixer.get_busy()):
    pass

pygame.mixer.quit()