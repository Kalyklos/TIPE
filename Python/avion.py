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
        """
        """
        self.fuel_cap = fuel_capacity
        self.fuel_cons = fuel_consumption
        self.etops = etops
        self.pos = position
        self.destination = None
    def new_destination(self, dest) :
        self.destination = dest