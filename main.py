import keylog
import time
#import getImage
import Mouselogger
#from Recorder_Son import Recorder, RecordingFile
import numpy as np
import json
import Request_Api as api
import scipy
import repeatedTime
import musicologie
import pymix

g_py = None
g_klog = None
g_mlog = None
g_getApi = None
g_getS = None
g_allData = []
g_rt = None
g_ApiActive=False
g_file = 'rawdata.csv'

def main():
    init()
    startAll()
    corpse()


def init():
    """This function instantiates all our global variables."""
    global g_klog, g_mlog, g_getApi, g_getS, g_rt, g_ApiActive, g_py
    g_klog = keylog.KeyLogger()
    g_mlog = Mouselogger.Mouselog()
    g_rt = repeatedTime.RepeatedTimer(1,dataHooker)
    g_py = pymix.Pymix()
    if g_ApiActive : g_getApi = api.Requests_Api()
    # g_getS = Recorder().open('Sortie_GetS.wav')
    print("Initialize")

def startAll():
    """Starts listening to the keyboard+mouse and recording the voice."""
    global g_klog, g_mlog, g_getS, g_ApiActive, g_py
    g_klog.start()
    g_mlog.start()
    # g_getS.start_recording()
    if g_ApiActive : g_getApi.update()
    g_py.add_feeling('calm')
    print("All Started")

def dataHooker():
    """Fills the 'g_allData' list with the different calculation functions implemented in classes."""
    global g_klog, g_mlog, g_getApi, g_getS, g_allData, g_rt
    if(g_klog.a_stopMain):
        # g_getS.stop_recording()
        g_klog.write_on_file('keylog.txt')
        database = np.asarray([
            g_klog.CountKey(), 
            g_mlog.getCumulTravelDistance(), 
            g_mlog.getRightMouseClicF(),
            # g_getS.amplitude(),
            0,
            0,
            0,
            0])

        if(g_ApiActive):
            for i in range(3):
                database[i+4]=g_getApi.Event_kill_life()[i]
            g_getApi.update()
            
        database[-1] = g_klog.a_state
     
        g_allData.append(database)
        
        print(g_allData[-1])
        print()
        resetAll()   
        # g_getS.start_recording()
        print(ia())
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
    f=open(g_file,'a')
    np.savetxt(f, g_allData, delimiter=';')
    f.close()

def resetAll():
    """Resets all internal class lists."""
    global g_klog, g_mlog, g_getApi, g_getS
    g_klog.reset()
    g_mlog.reset()
    if g_ApiActive : g_getApi.reset()

def ia():
    global g_py
    tab = g_allData[-2:]
    label = [ tab[0][-1],tab[1][-1] ]
    if label[0] == label[1]:
        if not (label[1] == g_py.state()):
            g_py.kill_feeling(g_py.state(),fade_out=3000)
            g_py.add_feeling(int(label[1]),fade_in=3000)

    return label

if __name__ == "__main__":
    main()