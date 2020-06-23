import keylog
import Mouselogger
import numpy as np
import Request_Api as api
import repeatedTime
import musicologie
import pymix
import collections
import pickle
#import tensorflow as tf
#from tensorflow import keras

#g_model = keras.models.load_model('model.h5')

g_py = None
g_klog = None
g_mlog = None
g_getApi = None
g_queue = collections.deque([0.0, 0.0, 0.0, 0.0, 0.0])
g_rt = None
g_ApiActive=False
g_file = 'rawdata.csv'
g_count = 0

try :
    g_normalize = pickle.load(open("normalize.dat", 'rb'))
except :
    g_normalize = [1.0,1.0,1.0,1.0,20.0,1.0]

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
    global g_klog, g_mlog, g_getApi, g_queue, g_rt, g_count
    if(g_klog.a_stopMain):
        database = np.asarray([
            g_klog.CountKey(),
            g_mlog.getCumulTravelDistance(),
            g_mlog.getRightMouseClicF(),
            0,
            0,
            0
        ])

        database = normalize(database)
        print(database)

        if(g_ApiActive):
            database.extend(g_getApi.event_kill_life())
            g_getApi.update()
        
        new_label = iaClassification( np.asarray(database) )

        if new_label == 1:
            g_count = 5

        if g_count:
            new_label = 1
            g_count = g_count - 1

        g_queue.append(new_label)

        #dans g_queue il y a les labels pour les musiques
        resetAll()

        if len(g_queue)>5 : 
            iaMusic(g_queue)
            taillemaxqueue(5,g_queue)
    else:
        stopAll()

def taillemaxqueue(max,queue):
  if len(queue)>max:
    queue.popleft()
    taillemaxqueue(max,queue)

def stopAll():
    """Stops all processes."""
    global g_klog, g_mlog, g_rt, g_queue, g_file
    g_klog.stop()
    g_mlog.stop()
    g_rt.stop()
    g_py.stop()

    pickle.dump(g_normalize, open("normalize.dat", 'wb'))

    print()
    print()
    print("All finished")

def resetAll():
    """Resets all internal class lists."""
    global g_klog, g_mlog, g_getApi
    g_klog.reset()
    g_mlog.reset()

def normalize(vector):
    global g_normalize
    # print(g_normalize)
    normalized = vector/g_normalize
    for i in range( len(normalized) ):
        if normalized[i] > 1:
            g_normalize[i] = vector[i]
    return vector/g_normalize

def iaClassification(vector, weight=[160,120,80,100,2000,0]):
    # vector = [countKeys, traveDistMouse, freqRightClic, deltaKills, deltaLife, isDead]
    global g_getApi, g_ApiActive
    if not len(vector) == len(weight):
        print("Warning : weight is not the same length than input vector !")
        return 0

    is_dead = vector[5]
    if is_dead:
        return 3

    print("function")
    print(np.sum(vector*weight))
    state = np.sum(vector*weight)
    if (state >= 100) :
        return 1
    return 0
    
    
def iaMusic(inputs,inertia=2):
    global g_py, g_getApi, g_ApiActive, g_queue

    labels = list(collections.deque(inputs))
    label = int(labels[-1])

    if g_ApiActive : event = g_getApi.output_event()
    else : event = -1
    if not event == -1:
        path = "musicologie/musiques/effects/" + event + "/"
        print(path)
        g_py.add_track_from_directory(path,channel=4)

    if not (labels[-1] == labels[-2]):
        g_py.kill_feeling( int(labels[-2]) )
        g_py.add_feeling(label)

    if not (g_py.is_busy()):
        label = labels[-1]
        g_py.add_feeling(int(label),fade_in=0)

    
    return g_py.get_feeling_busy()

if __name__ == "__main__":
    main()