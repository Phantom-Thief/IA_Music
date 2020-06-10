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

def main():

    init()
    startAll()
    time.sleep(5)
    dataHooker()
    time.sleep(2)
    stopAll()
    
    print(g_allData)
    # vector = np.zeros(5)
    # #[distance cumulée, fréquence clic, fréquence touche (+touches particulière), amplitude du son du micro, info API]
    # vector = test_threading(vector)
    # print(vector)

    # start_time = time.time()
    # lolApi = api.Requests_Api()
    # data = lolApi.select()
    # print(data['championStats']['currentHealth'])
    # print("--- %s seconds ---" % (time.time() - start_time))
    # lolApi.update()


def init():
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog = keylog.KeyLogger()
    g_mlog = Mouselogger.Mouselog()
    #g_getApi = api.Requests_Api()
    g_getS = Recorder().open('Sortie_GetS.wav')

def startAll():
    global g_klog, g_mlog, g_getS
    g_klog.start()
    g_mlog.start()
    g_getS.start_recording()

def dataHooker():
    global g_klog, g_mlog, g_getApi, g_getS, g_allData
    g_allData[:] = []
    appendInList(g_allData,[g_klog.CountKey(), g_mlog.getTravelDistance(), g_mlog.getCumulTravelDistance()])

def appendInList(li, tab):
    for i in tab:
        li.append(i)
    return 1

def stopAll():
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog.stop()
    g_mlog.stop()
    g_getS.stop_recording()

def resetAll():
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog.reset()
    g_mlog.reset()
    g_getApi.reset()


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
