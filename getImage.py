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
<<<<<<< HEAD
    
    def __init__(self):
        """
        constructeur de la classe GetImage avec comme attribut l'image qu'on veut stocker
        """
=======
    def __init__(self):
>>>>>>> master
        Thread.__init__(self)
        self.image = None
    
    def run(self):
        """
        méthode qui s'éxécute à chaque fois que l'on lance le Thread, ici le Thread prend un screen pendant 10 min 
        toutes les 0.5s
        """
        for n in range(1200):
            time.sleep(0.5)
            self.takeScreen("image.png")


<<<<<<< HEAD
    #Permet de prendre une capture d'écran et de la stocker dans un fichier dont on a passé le nom en paramètre et/ou
    #dans l'attribu image
=======
    def run(self):
        for n in range(1200):
            time.sleep(0.5)
            self.takeScreen("image.png")



>>>>>>> master
    def takeScreen(self,filename=None):
        if filename is None:
            self.image = pyscreeze.screenshot()
        else:
            self.image = pyscreeze.screenshot(filename)

