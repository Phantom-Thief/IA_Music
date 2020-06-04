import pynput
from scipy.spatial import distance
import numpy as np
from pynput.mouse import Button,Listener
from datetime import datetime

class Mouselog:
    def __init__(self):
        """
        move : list with all movement from the mouse
        clic : list with all clic and their position
        scroll : list with scroll's position and the direction of the scrolling
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

    def getTravelDistance(self):
        """
        return distance between the first and the last cursor's position
        """
        p1 = self.move[0][1]
        p2 = self.move[-1][1]
        return distance.euclidean(p1,p2)

    def getCumulTravelDistance(self):
        """
        return the whole distance traveled by the cursor
        """
        dist = []
        for i in range(len(self.move)-1):
            p1 = self.move[i][1]
            p2 = self.move[i+1][1]
            dist.append( distance.euclidean(p1,p2) )
        return np.sum(dist)

    def getMaxDistance(self):
        """
        return the distance between the two farthest points
        """
        points = []
        for i in self.move:
            points.append(i[1])
        p1 = np.min(points)
        p2 = np.max(points)
        return distance.euclidean(p1,p2)


    def on_move(self,x,y):
        """
        add logs and movement of mouse when it moves to the move list
        """
        log = ( datetime.now().time(), (x,y) )
        self.move.append(log)

    def on_click(self,x,y,button,pressed):
        """
        add logs and mouse's coordonates when a mouse's button is pressed or release
        """
        log = ( datetime.now().time(), (x,y) )
        self.clic.append(log)

    def on_scroll(self,x,y,dx,dy):
        """
        add logs, mouse's coordonates and movement's direction caused by scrolling when the mousewheel is used
        """
        log = ( datetime.now().time(), (x,y,dx,dy) )
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
                f.write(str(mov))
                f.write("\n")
            f.write(";\n")
            for cli in self.clic:
                f.write(str(cli))
                f.write("\n")
            f.write(";\n")
            for scro in self.scroll:
                f.write(str(scro))
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