#import module for screenshot
import pyscreeze
# Importing Image module from PIL package  
from PIL import Image  
import PIL

import datetime

  
im1 = pyscreeze.screenshot()

# save a image using extension 
im1 = im1.save( str(datetime.datetime.now()) ) 