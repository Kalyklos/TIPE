#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

# référencement de différents types d'avions représenté par des classes

import sys
import traceback
from typing import *
from math import *
from numpy import *

from settings import *
import way

class Plane :
    """C'EST DES NAVIONS ILS FONT VROOM VROOOOOOOOOM"""
    
    def __init__(self, fuel_capacity, fuel_consumption, etops, position) :
        """initializes

        Args : | fuel_Capacity of type float
               | fuel_consumption of type float
               | etops of type int
               | position of type Airport"""
        self.fuel_cap = fuel_capacity
        self.fuel = fuel_capacity
        self.fuel_cons = fuel_consumption
        self.etops = etops
        self.pos = position
        self.destination = None
    def new_destination(self, dest) :
        """Sets a new destination for the plane

        Args:
            dest (Airport): nouvelle destination
        """
        self.destination = dest
    def flight_time(self, current_fuel) :
        """returns flight capacity of self with current_fuel

        Args:
            current_fuel (int): la quantité de carburant

        Returns:
            float: flight time capacity with current_fuel
        """
        return self.fuel_cap/self.fuel_cons