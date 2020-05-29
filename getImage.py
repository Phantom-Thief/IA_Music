#import module for screenshot
import pyscreeze
# Importing Image module from PIL package  
from PIL import Image
import PIL

import datetime

class GetImage():
    def __init__(self):
        self.image = None

    def takeScreen(self):
        self.image = pyscreeze.screenshot()