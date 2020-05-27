#import module for screenshot
import pyscreeze
# Importing Image module from PIL package  
from PIL import Image  
import PIL  
   
  
im1 = pyscreeze.screenshot()
im2 = pyscreeze.screenshot('my_screenshot.png')

# save a image using extension 
im1 = im1.save("geeks.jpg") 