"""All imports necessary to carry out this process"""
import pynput
from pynput import keyboard
from datetime import datetime   


class KeyLogger:
    def __init__(self):
        """The builder of the 'KeyLogger' class

        Class for creating keyloggers and controlling them.
        'stopMain' is a boolean which detect the 'ù' and stop the main.py process
        A keylogger stores the received input logs in a 'a_keys' list.
        The 'listener' attribute will allow us to listen to the keyboard.
        State and find_state are used to determine the state of our recording.

        """
        self.a_stopMain = True
        self.a_keys = []
        self.a_listener = keyboard.Listener(on_press=self.on_press)
        self.a_state = 2
        self.a_find_state = {keyboard.Key.f1 : 0 ,keyboard.Key.f2 : 1 ,keyboard.Key.f3 : 2 ,keyboard.Key.f4 : 3}
                            # 0:joy 1:anger 2:calm 3:sadness
    def on_press(self,p_key):
        """Fills the list with a time and the key pressed."""
        if(p_key == keyboard.Key.alt_gr):
            self.a_stopMain = False
        if(p_key in self.a_find_state.keys()):
            self.a_state=self.a_find_state[p_key]
        else:
            log = ( datetime.now().time(), p_key )
            self.a_keys.append(log)
    
    def CountKey(self):
        """Return the number of keys pressed."""
        return len(self.a_keys)

    def getNumKeys(self,p_key):
        """Return the number of a given key (parameter)."""
        numKey = 0
        for i in self.a_keys:
            if p_key in str(i[1]):
                numKey +=1
        return numKey
       
    def write_on_file(self,p_filename):
        """Opens and fills a file with the list 'a_key'."""
        with open(p_filename,'a') as f:
            for key in self.a_keys:
                f.write(str(key))
                f.write("\n")
        f.close()

    def reset(self):
        self.a_keys[:] = []

    def start(self):
        """Starts the keylogger"""
        self.a_listener.start()

    def stop(self):
        """Stops the keylogger"""
        self.a_listener.stop()