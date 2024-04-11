#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

# référencement de différents types d'avions représenté par des classes

import sys
import traceback
from typing import *
from math import *
from numpy import *

from settings import *
ledictionnairedesetops = {}

class Plane :
    """Classe régissant les différents types d'avions simulable."""
    
    def __init__(self, fuel_capacity, fuel_consumption, etops, position, speed) :
        """initializes

        Args : | fuel_Capacity of type float (kg)
               | fuel_consumption of type float (kg.s^-1)
               | etops of type int
               | position of type Airport*Airport*x∈[0;1]
               | speed of type int"""
        self.fuel_cap = fuel_capacity
        self.fuel = fuel_capacity
        self.fuel_cons = fuel_consumption
        self.etops = etops
        self.pos = position
        self.speed = speed
        self.dest = None
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
    def fuel_alert(self) :
        if self.etops > self.flight_time_left() :
            return False
        return True
    def remove_s_fuel(self) :
        self.fuel = self.fuel-self.fuel_cons
    def remove_min_fuel(self) :
        self.fuel = self.fuel-60*self.fuel_cons
    def remove_h_fuel(self) :
        self.fuel = self.fuel-3600*self.fuel_cons
    def tick(self) :
        pass