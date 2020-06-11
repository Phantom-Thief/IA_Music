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
    #g_getApi = api.Requests_Api()
    g_getS = Recorder().open('Sortie_GetS.wav')

def startAll():
    """Starts listening to the keyboard+mouse and recording the voice."""
    global g_klog, g_mlog, g_getS
    g_klog.start()
    g_mlog.start()
    g_getS.start_recording()

def dataHooker():
    """Fills the 'g_allData' list with the different calculation functions implemented in classes."""
    global g_klog, g_mlog, g_getApi, g_getS, g_allData, g_rt
    if(g_klog.a_stopMain):
        g_getS.stop_recording()
        g_getS.amplitude()
        g_allData[:] = []
        appendInList(g_allData,[g_klog.CountKey(), g_mlog.getTravelDistance(), 
                                g_mlog.getCumulTravelDistance(), g_mlog.getRightMouseClicF(),
                                g_getS.moyenne(), g_getS.extremum()])
        print(g_allData)
        with open('result.txt','a') as f:
            f.write(str(g_allData))
            f.write('\n')
        resetAll()
        g_getS.start_recording()
    
    else:
        stopAll()

def appendInList(p_li, p_tab):
    """Function that adds an element of the array to the list in parameter."""
    for i in p_tab:
        p_li.append(i)
    return np.array(p_li)

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

if __name__ == "__main__":
    main()
