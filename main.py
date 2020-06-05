import keylog
import time
import getImage
import getSound
import Mouselogger

def main():

    # test_keylog(5)
    test_mouselog(5)
    # test_getImage()
    # test_getSound(2)
    #test_threading()
    pass

def test_threading(duration):
    klog = keylog.KeyLogger() 
    mlog = Mouselogger.Mouselog()
    getIm = getImage.GetImage()
    print("objets intanciés")
    klog.start()
    print("keylog lancé")
    mlog.start()
    print("mouselog lancé")
    getIm.start()
    print("Capture Image lancée")
    time.sleep(duration)
    klog.stop()
    print("keylog arrêté")
    mlog.stop()
    print("mouselog arrêté")
    getIm.join()
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
    print("dist1 : ")
    print(mlog.getTravelDistance())
    print("distCumul : ")
    print(mlog.getCumulTravelDistance())
    print("distMax : ")
    print(mlog.getMaxDistance())
    print("leftClicF : ")
    print(mlog.getLeftMouseClicF())
    print("rightClicF : ")
    print(mlog.getRightMouseClicF())

def test_getImage():
    screen = getImage.GetImage()
    screen.takeScreen()
    screen.takeScreen("test/image.png")

def test_getSound(duration):
    sound = getSound.getSound()
    sound.record(duration)
    sound.write_on_file("test/sound.wav")

if __name__ == "__main__":
    main()
