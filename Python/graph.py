#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

import sys
import traceback
from typing import *
from math import *

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from . import settings
from . import aeroport
from . import avion



try:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    from random import *

    Signal()
except ModuleNotFoundError as e:
    print("le module PySide6 devrait être installé pour que ce programme puisse fonctionner, lisez README.md pour plus de détails", file=stderr)
    raise e


class Graph :
    """Airports link"""
    
    def __init__(self, width) :
        self.values = [[0 for j in range(width)] for i in range(width)]
        #on identifie les aéroports par les noeuds du graphe, en les modélisant par une matrice.

        self.n_airports = width
        self.nom_noeud_graph = [] #on stockera les initiales des aéroports dans une list de str.
    
    def new_airport(self) :
        """None --> Graph
        Adds a new Airport to the Graph"""
        
        self.n_airports += 1
        self.values.append([0 for i in range(self.n_airports)])
        for i in range(self.n_airports-1) :
            self.values[i].append(0)
    
    
    def new_link(self, airport1, airport2, cost) :
        """Airport_Id, Airport_Id, Int --> Graph
        If no links exist between airport1 and airport2, adds a new link of weight cost between Airport1 and Airport2"""
        
        if self.values[airport1][airport2] == 0 :
            self.values[airport1][airport2] = cost
            self.values[airport2][airport1] = cost
        
    
    def __str__(self) :
        """outputs a pretty string.
        how pretty ?  not as much as you <3"""
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



NY = aeroport.Airport(9)
print(NY.nb_runway)
