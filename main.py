import keylog
import time
import getImage
import Mouselogger
from Recorder_Son import Recorder, RecordingFile
import numpy as np
import json
import Request_Api as api
import scipy
import repeatedTime

g_klog = None
g_mlog = None
g_getApi = None
g_getS = None
g_allData = []
g_rt = None

def main():
    init()
    startAll()
    corpse()


def init():
    """This function instantiates all our global variables."""
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog = keylog.KeyLogger()
    g_mlog = Mouselogger.Mouselog()
    g_getApi = api.Requests_Api()
    g_getS = Recorder().open('Sortie_GetS.wav')

def startAll():
    """Starts listening to the keyboard+mouse and recording the voice."""
    global g_klog, g_mlog, g_getS
    g_klog.start()
    g_mlog.start()
    g_getS.start_recording()

def dataHooker():
    """Fills the 'g_allData' list with the different calculation functions implemented in classes. """
    global g_klog, g_mlog, g_getApi, g_getS, g_allData
    g_allData[:] = []
    appendInList(g_allData,[g_klog.CountKey(), g_mlog.getTravelDistance(), g_mlog.getCumulTravelDistance()])

def appendInList(p_li, p_tab):
    """Function that adds an element of the array to the list in parameter"""
    for i in p_tab:
        p_li.append(i)
    return 1

def corpse(duration):
    """Periodically call 'dataHooker' which fills the 'g_allData' list."""
    g_rt = repeatedTime.RepeatedTimer(1,dataHooker)

def stopAll():
    """stops all processes"""
    global g_klog, g_mlog, g_getS, g_rt
    g_klog.stop()
    g_mlog.stop()
    g_getS.stop_recording()
    g_rt.stop()

def resetAll():
    """resets all internal class lists"""
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog.reset()
    g_mlog.reset()
    g_getApi.reset()
    g_rt.stop()


def test_threading(vector):
    recordTime = 10

    klog = keylog.KeyLogger() 
    mlog = Mouselogger.Mouselog()
    #getIm = getImage.GetImage()
    GetS = Recorder()
   
    S = GetS.open('Sortie_GetS.wav')
    S.start_recording()
    print("Lancement du son")


    print("objets intanciés")
    klog.start()
    print("keylog lancé")
    mlog.start()
    print("mouselog lancé")
    rt = repeatedTime.RepeatedTimer(1,hello,"Test")
    print("Timer lancé lets go")
   

    time.sleep(recordTime)
    print("hop hop on stop le record")
    S.stop_recording()
    #Donne les amplitudes du fichiers wav courant
    #S.amplitude()

    klog.stop()
    print("keylog arrêté")
    mlog.stop()
    print("mouselog arrêté")
    rt.stop()
    print("Timer stop")

    klog.write_on_file("keyboard.txt")
    mlog.write_on_file("mouse.txt")

    vector[0] = mlog.getCumulTravelDistance()/2202
    vector[1] = mlog.getNbSample()[1]/recordTime
    vector[2] = klog.CountKey()/recordTime
    vector[3] = S.amplitude()
    vector[4] = 0

    return vector

def test_keylog(waittime):
    klog = keylog.KeyLogger()
    klog.start()
    time.sleep(waittime)
    klog.stop()
    klog.write_on_file("test/keyboard.txt")
    # print(klog.keys)

def test_mouselog(waittime):
    mlog = Mouselogger.Mouselog()
    mlog.start()
    time.sleep(waittime)
    mlog.stop()
    mlog.write_on_file("test/mouse.txt")
    # print(mlog.move)
    # print(mlog.clic)
    # print(mlog.scroll)

def test_getImage():
    screen = getImage.GetImage()
    screen.takeScreen()
    screen.takeScreen("test/image.png")

def hello(name):
    print(name)

if __name__ == "__main__":
    main()
