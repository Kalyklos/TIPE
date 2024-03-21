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



# try:
#     from PySide6.QtCore import *
#     from PySide6.QtWidgets import *
#     from PySide6.QtGui import *

#     Signal()
# except ModuleNotFoundError as e:
#     print("le module PySide6 devrait être installé pour que ce programme puisse fonctionner, lisez README.md pour plus de détails", file=stderr)
#     raise e

class Graph :
    """Airports link"""
    def __init__(self, vertices) :
        """init de la class Graph

        Args:
            width (int): Nombre d'aéroports
            vertices (int): Nombre d'arêtes
        """
        self.M = vertices   # Nombre d'arêtes
        self.graph = []     # tableau de noeuds
        
    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])

    def print_solution(self, distance):
        print("Distance :")
        for k in range(self.M):
            print("{0}\t\t{1}".format(k, distance[k]))

    def bellman_ford(self, src):
        distance = [float("Inf")] * self.M
        distance[src] = 0
        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c
        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("Euhh problème")
                return
        self.print_solution(distance)

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
            str: le nom des aéroports
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

g = Graph(5)
g.add_edge(0, 7, 2)
g.add_edge(0, 6, 4)
g.add_edge(1, 9, 7)
g.add_edge(2, 4, 3)
g.add_edge(2, 3, 4)
g.add_edge(4, 3, -5)

g.bellman_ford(0)