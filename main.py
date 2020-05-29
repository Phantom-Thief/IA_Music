import keylog
import time
#import getImage
#import getSound
import Mouselogger

def main():

    #test_keylog(1)
    test_mouselog(1)


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


if __name__ == "__main__":
    main()