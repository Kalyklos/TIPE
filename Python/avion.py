#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

# référencement de différents types d'avions représenté par des classes

import sys
import traceback
from typing import *
from math import *
from numpy import *

from settings import *
from graph import *
ledictionnairedesetops = {}

class Plane :
    """Classe régissant les différents types d'avions simulable."""
    
    def __init__(self, fuel_capacity, fuel_consumption, etops, position, speed) :
        """initializes

        Args : | fuel_Capacity of type float (kg)
               | fuel_consumption of type float (kg.s^-1)
               | etops of type int
               | position of type Airport*Airport*x∈[0;1]
               | speed of type int (m.s^-1)"""
        self.fuel_cap = fuel_capacity
        self.fuel = fuel_capacity
        self.fuel_cons = fuel_consumption
        self.etops = etops
        self.pos = position
        self.speed = speed
        self.dest = None
        self.chemin = []
    def new_destination(self, dest) :
        """Sets a new destination for the plane

        Args:
            dest (Airport): nouvelle destination
        """
        self.dest = dest
    def flight_time_left(self) :
        """returns flight capacity of self with current_fuel

        Args:
            current_fuel (int): la quantité de carburant

        Returns:
            float: flight time capacity with current_fuel
        """
        return self.fuel/self.fuel_cons
    def etops_assert(self, route) :
        """checks if the plane has required etops for route

        Args:
            route (Airport*Airport): route trying to be taken

        Returns:
            bool: True if self has clearance for route, False elsewise
        """
        if self.etops >= ledictionnairedesetops[route] : #to do : créer ledictonnairedesetops
            return True
        return False
    def remove_s_fuel(self) :
        """removes 1s worth of fuel
        """
        self.fuel = self.fuel-self.fuel_cons
    def remove_min_fuel(self) :
        """removes 1min worth of fuel
        """
        self.fuel = self.fuel-60*self.fuel_cons
    def remove_h_fuel(self) :
        """removes 1h worth of fuel
        """
        self.fuel = self.fuel-3600*self.fuel_cons
    def ptick(self) :
        """simulates one tick for the plane
        """
        newtruc = self.speed*60/graph[self.pos[0]][self.pos[1]]
        if self.pos[2] + newtruc < 1 :
            self.pos[2] += newtruc
        else :
            self.pos[0] = self.pos[1]
            self.pos[1] = self.chemin[0]
            self.chemin = self.chemin[1, :]
            self.pos[2] = self.pos[2] + newtruc - 1