import pynput
from pynput.mouse import Button,Listener
from datetime import datetime

class Mouselog:
    def __init__(self):
        self.move = []
        self.clic = []
        self.scroll = []

        def on_move(x,y):
            log = str(datetime.now().time()) + " " + str((x,y))
            self.move.append(log)

        def on_click(x,y,button,pressed):
            log = str(datetime.now().time()) + " " + str((x,y))
            self.clic.append(log)

        def on_scroll(x,y,dx,dy):
            log = str(datetime.now().time()) + " " + str((x,y,dx,dy))
            self.scroll.append(log)

        self.listener = Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)


    def mouseLogger():
        with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
            listener.join()

    def write_on_file(self, filename):
        with open(filename,'w') as f:
            for mov in self.move:
                f.write(mov)
                f.write("\n")
            f.write(";\n")
            for cli in self.clic:
                f.write(cli)
                f.write("\n")
            f.write(";\n")
            for scro in self.scroll:
                f.write(scro)
                f.write("\n")
            f.write(";")

    def start(self):
        """
        permet de démarrer le mouselogger
        """
        self.listener.start()

    def stop(self):
        """
        permet d'arrêter le mouselogger
        """
        self.listener.stop()
