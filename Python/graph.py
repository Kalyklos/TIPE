#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

import sys
import traceback
from typing import *
from math import *
from numpy import *

from settings import *
from aeroport import *
from way import *


class Graph :
    """Airports link"""
    def __init__(self, width) :
        """init de la class Graph

        Args:
            width (int): nombre de sommets (aéroports)
        """
        
        self.n_airports = width  # to do ajouter self.link un dictionnaire de dictionnaire contenant pour chaque aeroport les liens direct avec les aeroports et leur distance (distance par rapport à soi-même = 0).
        self.values = [[inf for j in range(width)] for i in range(width)]
        for i in range(self.n_airports) :
            self.values[i][i] = 0
    
    
    def new_airport(self) :
        """None --> Graph
        Adds a new Airport to the Graph"""
        
        self.n_airports += 1
        self.values.append([-1 for i in range(self.n_airports)])
        for i in range(self.n_airports-1) :
            self.values[i].append(inf)
        self.values[self.n_airports-1][self.n_airports-1] = 0
    
    
    def add_link(self, airport1, airport2, cost) :
        """Airport_Id, Airport_Id, Int --> Graph
        If no links exist between airport1 and airport2, adds a new link of weight cost between Airport1 and Airport2"""
        
        if self.values[airport1][airport2] == inf :
            self.values[airport1][airport2] = cost
            self.values[airport2][airport1] = cost
        
    
    def __str__(self) :
        """affiche le nom des aéroports

        Returns:
            str: string représentant le graphe à afficher
        """
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


g2 = Graph(2)
g3 = Graph(3)
g10 = Graph(10)
graph = Graph(0)

g2.add_link(0,1,1)

g3.add_link(0,1,1)
g3.add_link(1,2,0.5)
g3.add_link(0,2,2)

g10.add_link(0,1,5)
g10.add_link(0,2,7.5)
g10.add_link(0,6,16)
g10.add_link(1,5,12)
g10.add_link(2,4,13)
g10.add_link(3,5,2)
g10.add_link(4,5,6)
g10.add_link(4,9,11)
g10.add_link(5,7,4)
g10.add_link(6,8,1.5)
g10.add_link(7,8,0.75)
g10.add_link(8,9,4)