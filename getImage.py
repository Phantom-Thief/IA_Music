#import module for screenshot
import pyscreeze
# Importing Image module from PIL package  
import PIL
#from PIL import Image

import datetime

class GetImage():
    def __init__(self):
        self.image = None

    def takeScreen(self,filename=None):
        if filename is None:
            self.image = pyscreeze.screenshot()
        else:
            self.image = pyscreeze.screenshot(filename)
