#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

# référencement de différents types d'avions représenté par des classes

import sys
import traceback
from typing import *
from math import *

from settings import *

class Plane :
    """C'EST DES NAVIONS ILS FONT VROOM VROOOOOOOOOM"""
    
    def __init__(self, fuel_capacity, fuel_consumption, etops, position) :
        assert type(fuel_capacity) == float, "fuel_capacity has to be of type float"
        assert type(fuel_consumption) == float, "fuel_consumption has to be an float"
        assert type(etops) == int, "etops has to be an integer"
        
        self.fuel_cap = fuel_capacity
        self.fuel_cons = fuel_consumption
        self.etops = etops
        self.pos = position
