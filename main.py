import keylog
import time
import Mouselogger
import numpy as np
import json
import Request_Api as api
import scipy
import repeatedTime
import musicologie
import pymix
import queue

g_py = None
g_klog = None
g_mlog = None
g_getApi = None
#Changement sans fichier intermedaire g_allData = queue.Queue(maxsize=2)
g_allData = []
g_rt = None
g_ApiActive=False
g_file = 'rawdata.csv'

def main():
    init()
    startAll()


def init():
    """This function instantiates all our global variables."""
    global g_klog, g_mlog, g_getApi,  g_rt, g_ApiActive, g_py
    g_klog = keylog.KeyLogger()
    g_mlog = Mouselogger.Mouselog()
    g_rt = repeatedTime.RepeatedTimer(1,dataHooker)
    g_py = pymix.Pymix()
    if g_ApiActive : g_getApi = api.Requests_Api()
    print("Initialize")

def startAll():
    """Starts listening to the keyboard+mouse and recording the voice."""
    global g_klog, g_mlog, g_ApiActive, g_py, g_rt
    g_klog.start()
    g_mlog.start()

    if g_ApiActive : g_getApi.update()
    g_py.add_track('musicologie/musiques/effects/high_tech_start.wav')
    g_py.add_feeling('calm',fade_in=10000)
    g_rt.start()
    print("All Started")

def dataHooker():
    """Fills the 'g_allData' list with the different calculation functions implemented in classes."""
    global g_klog, g_mlog, g_getApi, g_allData, g_rt
    if(g_klog.a_stopMain):
        database = np.asarray([
            g_klog.CountKey(), 
            g_mlog.getCumulTravelDistance(), 
            g_mlog.getRightMouseClicF(),
            0,
            0,
            0,
            0])

        if(g_ApiActive):
            for i in range(3):
                database[i+4]=g_getApi.event_kill_life()[i]
            g_getApi.update()
            
        database[-1] = g_klog.a_state
     
        # Changement g_allData.put(database,block=False)
        """La file créée est une file de 2 élements (mode FIFO) pour sortir l'élément qui est rentré en premier,
            Il faut utiliser g_allData.get(block=False) ce qui renvoie et enlève la premiere donnée rentrée dans la file
        """
        g_allData.append(database)
        
        resetAll()  
        
        label = [i[-1] for i in g_allData]

        if len(label)>3 : iaMusic(label)
    else:
        stopAll()


def stopAll():
    """Stops all processes."""
    global g_klog, g_mlog, g_rt, g_allData, g_file, g_py
    g_klog.stop()
    g_mlog.stop()
    g_rt.stop()
    f=open(g_file,'a')
    np.savetxt(f, g_allData, delimiter=';')
    f.close()
    g_py.stop()
    print()
    print()
    print("All finished")

def resetAll():
    """Resets all internal class lists."""
    global g_klog, g_mlog, g_getApi
    g_klog.reset()
    g_mlog.reset()

def iaMusic(input,inertia=2):
    global g_py, g_getApi

    labels = input[-inertia:]

    # if g_getApi.event_kill_life()[2]:
    #     labels[-inertia:] = 3

    if labels.count(labels[-1]) == len(labels) and labels:
        label = int(labels[-1])
        if not (label == input[-inertia-1]):
            g_py.kill_feeling( int(input[-inertia-1]) )
            g_py.add_feeling(label)

    if not (g_py.is_busy()):
        g_py.add_feeling(label,fade_in=0)

    return g_py.get_feeling_busy()

if __name__ == "__main__":
    main()