import time
import numpy as np

from way import *
from avion import *
from aeroport import *
from graph import *
from affichage import *

class Sim :
    def __init__(self, G, tab_navions) :
        """intiates the simulation

        Args:
            G (Graph (see Graph.py)): the graph in which the simulation takes place, fixed
            tab_navions (Plane array): lists all the planes currently running through the simulation
        """
        self.tick = 0                       #the current tick of the simulation
        self.graph = G                      #graph of the sim
        self.planes = tab_navions           #list of the planes in the sim
        self.tickspeed = 1                  #number of ticks per second
    
    def set_tickspeed(self, ts) :
        """changes the tickspeed of the simulation

        Args:
            ts (int): neww tickspeed
        """
        self.tickspeed = ts
    
    def new_plane(self, plane) :
        """adds a new plane in the simulation

        Args:
            plane (Plane): the plane to be added to the sim
        """
        self.planes.append(plane)