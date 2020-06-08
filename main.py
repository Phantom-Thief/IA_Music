import keylog
import time
import getImage
import Mouselogger
from Recorder_Son import Recorder, RecordingFile
import numpy as np

def main():

    vector = np.zeros(5)
    #[distance cumulée, fréquence clic, fréquence touche (+touches particulière), amplitude du son du micro, info API]
    vector = test_threading(vector)
    print(vector)



def test_threading(vector):
    recordTime = 5

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
    

    time.sleep(recordTime)
    print("hop hop on stop le record")
    S.stop_recording()
    #Donne les amplitudes du fichiers wav courant
    #S.amplitude()

    klog.stop()
    print("keylog arrêté")
    mlog.stop()
    print("mouselog arrêté")

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

if __name__ == "__main__":
    main()
