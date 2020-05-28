#import module for screenshot
import pyscreeze
# Importing Image module from PIL package  
from PIL import Image
import PIL

import datetime

im1 = pyscreeze.screenshot()

#build image name
name = str(datetime.datetime.now())
name = name.replace('-','_')
name = name.replace(':','_')
dot= name.find('.')
name = name[:dot]+".jpeg"
# save a image using extension
im1 = im1.save(name)