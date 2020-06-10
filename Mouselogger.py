"""All imports necessary to carry out this process"""
import pynput
from scipy.spatial import distance
import numpy as np
from pynput.mouse import Button,Listener
from datetime import datetime

class Mouselog:
    def __init__(self):
        """The builder of the 'Mouselog' class

        attribute list:
        move : list with all movement from the mouse
        clic : list with all clic and their position
        scroll : list with scroll's position and the direction of the scrolling
        listener : object used to listen mouse's activities

        """
        self.a_move = []
        self.a_clic = []
        self.a_scroll = []
        self.a_listener = Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

    def getMove(self):
        """Returns the attribute 'a_move'."""
        return self.a_move

    def getClic(self):
        """Returns the attribute 'a_clic'."""
        return self.a_clic

    def getScroll(self):
        """Returns the attribute 'a_scroll'."""
        return self.a_scroll

    def getNbSample(self):
        """Return a tuple with the number of samples in each list."""
        return ( len(self.a_move),len(self.a_clic),len(self.a_scroll) )

    def getTravelDistance(self):
        """Return distance between the first and the last cursor's position."""
        try:
            p1 = self.a_move[0][1]
            p2 = self.a_move[-1][1]
            return distance.euclidean(p1,p2)
        except:
            return 0

    def getCumulTravelDistance(self):
        """Return the whole distance traveled by the cursor."""
        dist = []
        try:
            for i in range(len(self.a_move)-1):
                p1 = self.a_move[i][1]
                p2 = self.a_move[i+1][1]
                dist.append( distance.euclidean(p1,p2) )
            return np.sum(dist)
        except:
            return 0

    def getMaxDistance(self):
        """Return the distance between the two farthest points."""
        points = []
        try:
            for i in self.a_move:
                points.append(i[1])
            p1 = np.min(points,axis=0)
            p2 = np.max(points,axis=0)
            return distance.euclidean(p1,p2)
        except:
            return 0

    def getLeftMouseClicF(self):
        """Return the number of left clic."""
        leftClic = []
        try:
            for i in self.a_clic:
                if "left" in str(i[2]):
                    leftClic.append(i)
            return len(leftClic)
        except:
            return 0

    def getRightMouseClicF(self):
        """Return the number of right clic."""
        rightClic = []
        try:
            for i in self.a_clic:
                if "right" in str(i[2]):
                    rightClic.append(i)
            return len(rightClic)
        except:
            return 0

    def on_move(self,p_x,p_y):
        """Add logs and movement of mouse when it moves to the move list."""
        log = ( datetime.now().time(), (p_x,p_y) )
        self.a_move.append(log)

    def on_click(self,p_x,p_y,p_button,p_pressed):
        """Add logs and mouse's coordonates when a mouse's button is pressed or release."""
        if p_pressed:
            log = ( datetime.now().time(), (p_x,p_y), p_button )
            self.a_clic.append(log)

    def on_scroll(self,p_x,p_y,p_dx,p_dy):
        """Add logs, mouse's coordonates and movement's direction caused by scrolling when the mousewheel is used."""
        log = ( datetime.now().time(), (p_x,p_y,p_dx,p_dy) )
        self.a_scroll.append(log)

    def write_on_file(self, p_filename):
        """Write all list's content in a file.
        
        It starts with the list move, then clic, then scroll;
        Each list is separate by ";"
        Each sample is separate by "\n"

        """
        with open(p_filename,'w') as f:
            for mov in self.a_move:
                f.write(str(mov))
                f.write("\n")
            f.write(";\n")
            for cli in self.a_clic:
                f.write(str(cli))
                f.write("\n")
            f.write(";\n")
            for scro in self.a_scroll:
                f.write(str(scro))
                f.write("\n")
            f.write(";")

    def reset(self):
        self.a_move[:] = []
        self.a_clic[:] = []
        self.a_scroll[:] = []

    def start(self):
        """Starts the mouselogger in a thread."""
        self.a_listener.start()

    def stop(self):
        """Stops the mouselogger's thread."""
        self.a_listener.stop()