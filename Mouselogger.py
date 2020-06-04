import pynput
from pynput.mouse import Button,Listener
from datetime import datetime

class Mouselog:
    def __init__(self):
        """
        move : list with all movement from the mouse
        clic : list with all clic and their position
        scroll : list with scroll's position and delta created by scrolling
        listener : object used to listen mouse's activities
        """
        self.move = []
        self.clic = []
        self.scroll = []
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

    def getMove(self):
        return self.move

    def getClic(self):
        return self.clic

    def getScroll(self):
        return self.scroll

    def getNbSample(self):
        """
        return a tuple with the number of samples in each list
        """
        return ( len(self.move),len(self.clic),len(self.scroll) )

    def on_move(self,x,y):
        """
        add logs and movement of mouse when it moves to the move list
        """
        log = str(datetime.now().time()) + " " + str((x,y))
        self.move.append(log)

    def on_click(self,x,y,button,pressed):
        """
        add logs and mouse's coordonates when a mouse's button is pressed or release
        """
        log = str(datetime.now().time()) + " " + str((x,y))
        self.clic.append(log)

    def on_scroll(self,x,y,dx,dy):
        """
        add logs, mouse's coordonates and movement caused by scrolling when the mousewheel is used
        """
        log = str(datetime.now().time()) + " " + str((x,y,dx,dy))
        self.scroll.append(log)

    def write_on_file(self, filename):
        """
        write all list's content in a file
        it starts with the list move, then clic, then scroll
        each list is separate by ";"
        eache sample is separate by "\n"
        """
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
        starts the mouselogger in a thread
        """
        self.listener.start()

    def stop(self):
        """
        stops the mouselogger's thread
        """
        self.listener.stop()