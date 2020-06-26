#import module for screenshot
import pyscreeze
# Importing Image module from PIL package  
import PIL
#from PIL import Image
from threading import Thread
#utilistation de thread pour faire des images
import time


import datetime

class GetImage(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.image = None

    def run(self):
        for n in range(1200):
            time.sleep(0.5)
            self.takeScreen("image.png")



    def takeScreen(self,filename=None):
        if filename is None:
            self.image = pyscreeze.screenshot()
        else:
            self.image = pyscreeze.screenshot(filename)
