import keylog
import time
#import getImage
import Mouselogger
from Recorder_Son import Recorder, RecordingFile
import numpy as np
import json
import Request_Api as api
import scipy
import repeatedTime
import musicologie

g_klog = None
g_mlog = None
g_getApi = None
g_getS = None
g_allData = []
g_rt = None
g_ApiActive=False

def main():
    init()
    startAll()
    corpse()


def init():
    """This function instantiates all our global variables."""
    global g_klog, g_mlog, g_getApi, g_getS, g_rt
    g_klog = keylog.KeyLogger()
    g_mlog = Mouselogger.Mouselog()
    g_rt = repeatedTime.RepeatedTimer(1,dataHooker)
    g_getApi = api.Requests_Api()
    g_getS = Recorder().open('Sortie_GetS.wav')

def startAll():
    """Starts listening to the keyboard+mouse and recording the voice."""
    global g_klog, g_mlog, g_getS, g_ApiActive
    g_klog.start()
    g_mlog.start()
    g_getS.start_recording()
    if(g_ApiActive):
        g_getApi.update()

def dataHooker():
    """Fills the 'g_allData' list with the different calculation functions implemented in classes."""
    global g_klog, g_mlog, g_getApi, g_getS, g_allData, g_rt
    if(g_klog.a_stopMain):
        if(g_ApiActive):
            g_getS.stop_recording()
            g_allData.append( np.asarray([g_klog.CountKey(), g_mlog.getTravelDistance(), 
                                    g_mlog.getCumulTravelDistance(), g_mlog.getRightMouseClicF(),
                                    g_getS.amplitude()]) )
        
            print(g_allData)
            resetAll()
            g_getS.start_recording()

        else:
            g_getS.stop_recording()
            g_allData.append( np.asarray([g_klog.CountKey(), g_mlog.getTravelDistance(), 
                                    g_mlog.getCumulTravelDistance(), g_mlog.getRightMouseClicF(),
                                    g_getS.amplitude()]) ) #######rajouter l'API DE LOL
        
            print(g_allData)
            resetAll()
            g_getS.start_recording()
    
    else:
        knn(np.asarray(g_allData))
        stopAll()


def corpse():
    """Periodically call 'dataHooker' which fills the 'g_allData' list."""
    g_rt.start()



def stopAll():
    """Stops all processes."""
    global g_klog, g_mlog, g_getS, g_rt
    g_klog.stop()
    g_mlog.stop()
    g_rt.stop()
    g_getS.stop_recording()
    g_getS.close()

def resetAll():
    """Resets all internal class lists."""
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog.reset()
    g_mlog.reset()
    #g_getApi.reset()

def knn(data):
    print(data)

if __name__ == "__main__":
    main()