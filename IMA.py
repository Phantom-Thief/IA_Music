import os
import sys
import updater

try : updater.updater()
except: pass


os.system("python IMA/Gui.py")