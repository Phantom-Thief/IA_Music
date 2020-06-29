import os
import sys
sys.path.append('/IMA')
"""
Ce fichier sera l'exécutable
"""

import updater

try : updater.updater()
except: pass


os.system("python IMA/Gui.py")
quit()