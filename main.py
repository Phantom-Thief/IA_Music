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
g_ApiActive=True
g_file = 'data.csv'

def main():
    init()
    startAll()
    corpse()


def init():
    """This function instantiates all our global variables."""
    global g_klog, g_mlog, g_getApi, g_getS, g_rt, g_ApiActive
    g_klog = keylog.KeyLogger()
    g_mlog = Mouselogger.Mouselog()
    g_rt = repeatedTime.RepeatedTimer(1,dataHooker)
    if g_ApiActive : g_getApi = api.Requests_Api()
    # g_getS = Recorder().open('Sortie_GetS.wav')
    print("Initialize")

def startAll():
    """Starts listening to the keyboard+mouse and recording the voice."""
    global g_klog, g_mlog, g_getS, g_ApiActive
    g_klog.start()
    g_mlog.start()
    # g_getS.start_recording()
    if g_ApiActive : g_getApi.update()
    print("All Started")

def dataHooker():
    """Fills the 'g_allData' list with the different calculation functions implemented in classes."""
    global g_klog, g_mlog, g_getApi, g_getS, g_allData, g_rt
    if(g_klog.a_stopMain):
        # g_getS.stop_recording()
        database = np.asarray([
            g_klog.CountKey(), 
            g_mlog.getTravelDistance(), 
            g_mlog.getCumulTravelDistance(), 
            g_mlog.getRightMouseClicF(),
            # g_getS.amplitude(),
            0,
            0,
            0,])

        if(g_ApiActive):
            # listelol = g_getApi.Event_kill_life().append(g_getApi.output())
            for i in range(3):
                database[i+4]=g_getApi.Event_kill_life()[i]
            g_getApi.update()

     
        g_allData.append(database)
        
        print(g_allData)   
        resetAll()   
        # g_getS.start_recording()
    
    else:
        stopAll()


def corpse():
    """Periodically call 'dataHooker' which fills the 'g_allData' list."""
    g_rt.start()



def stopAll():
    """Stops all processes."""
    global g_klog, g_mlog, g_getS, g_rt, g_allData, g_file
    g_klog.stop()
    g_mlog.stop()
    g_rt.stop()
    # g_getS.stop_recording()
    # g_getS.close()
    np.savetxt(g_file, g_allData, delimiter=';')

def resetAll():
    """Resets all internal class lists."""
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog.reset()
    g_mlog.reset()
    #g_getApi.reset()

if __name__ == "__main__":
    main()