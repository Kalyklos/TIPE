#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

import sys
import traceback
from typing import *
from math import *
from numpy import *

from settings import *
from aeroport import *
from avion import *



try:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *

    Signal()
except ModuleNotFoundError as e:
    print("le module PySide6 devrait être installé pour que ce programme puisse fonctionner, lisez README.md pour plus de détails", file=stderr)
    raise e


class Graph :
    """Airports link"""
    def __init__(self, width) :
        # to do : DOCUMENTE TES FONCTIONS !!!
        
        self.n_airports = width  # to do ajouter self.link un dictionnaire de dictionnaire contenant pour chaque aeroport les liens direct avec les aeroports et leur distance (distance par rapport à soi-même = 0).
        self.values = [[-1 for j in range(width)] for i in range(width)]
        for i in range(self.n_airports) :
            self.values[i][i] = 0
    
    
    def new_airport(self) :
        """None --> Graph
        Adds a new Airport to the Graph"""
        
        self.n_airports += 1
        self.values.append([-1 for i in range(self.n_airports)])
        for i in range(self.n_airports-1) :
            self.values[i].append(-1)
        self.values[self.n_airports-1][self.n_airports-1] = 0
    
    
    def add_link(self, airport1, airport2, cost) :
        """Airport_Id, Airport_Id, Int --> Graph
        If no links exist between airport1 and airport2, adds a new link of weight cost between Airport1 and Airport2"""
        
        if self.values[airport1][airport2] == -1 :
            self.values[airport1][airport2] = cost
            self.values[airport2][airport1] = cost
        
    
    def __str__(self) :
        # non tu DOCUMENTE tes fonctions
        string = "\n"
        for i in self.values :
            string += "|"
            for j in i :
                string += str(j)
                string += ", "
            string = string[:-1]
            string = string[:-1]
            string += "|\n"
        return string


def graph_creation(n) :
    G = Graph(n)