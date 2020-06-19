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
import collections
from tensorflow import keras
from Dictionnaire import pyApi

g_model = keras.models.load_model('model.h5')

g_py = None
g_klog = None
g_mlog = None
g_getApi = None
g_queue = collections.deque([])
g_rt = None
g_ApiActive=True
g_file = 'rawdata.csv'

def main():
    init()
    startAll()

def init():
    """This function instantiates all our global variables."""
    global g_klog, g_mlog, g_getApi, g_rt, g_ApiActive, g_py
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
    """Fills the 'g_queue' list with the different calculation functions implemented in classes."""
    global g_klog, g_mlog, g_getApi, g_queue, g_rt
    if(g_klog.a_stopMain):
        database = np.asarray([
            g_klog.CountKey(), 
            g_mlog.getCumulTravelDistance(), 
            g_mlog.getRightMouseClicF(),
            0,
            0,
            0])

        if(g_ApiActive):
            for i in range(3):
                database[i+3]=g_getApi.event_kill_life()[i]
            g_getApi.update()
        
        g_queue.append(iaClassification( np.asarray([database]) ))
        #dans g_queue il y a les labels pour les musiques
        resetAll()
        
        label = [i for i in list(g_queue)]

        if len(label)>3 : 
            iaMusic(label)
            taillemaxqueue(3,g_queue)
    else:
        stopAll()

def taillemaxqueue(max,queue):
  if len(queue)>max:
    queue.popleft()
    taillemaxqueue(max,queue)

def stopAll():
    """Stops all processes."""
    global g_klog, g_mlog, g_rt, g_queue, g_file, g_py
    g_klog.stop()
    g_mlog.stop()
    g_rt.stop()
    g_py.stop()
    print()
    print()
    print("All finished")

def resetAll():
    """Resets all internal class lists."""
    global g_klog, g_mlog, g_getApi
    g_klog.reset()
    g_mlog.reset()

def iaClassification(vector):
    global g_model, g_getApi
    print(g_getApi.output_event())
    if g_getApi.event_kill_life()[2] == 1: return 3
    label = g_model.predict(vector)
    return label
    
def iaMusic(input,inertia=2):
    global g_py, g_getApi
    labels = input[-inertia:]

    event = g_getApi.output_event()
    if not event == -1:
        path = "musicologie/musiques/effects/" + event + "/"
        print(path)
        g_py.add_track_from_directory(path,channel=4)


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