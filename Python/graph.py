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
    def __init__(self, width, vertices) :
        """init de la class Graph

        Args:
            width (int): Nombre d'aéroports
            vertices (int): Nombre d'arêtes
        """
        self.M = vertices   # Nombre d'arêtes
        self.graph = []     # tableau de noeuds
        self.n_airports = width  # to do ajouter self.link un dictionnaire de dictionnaire contenant pour chaque aeroport les liens direct avec les aeroports et leur distance (distance par rapport à soi-même = 0).
        self.values = [[inf for j in range(width)] for i in range(width)]
        for i in range(self.n_airports) :
            self.values[i][i] = 0
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

g2 = Graph(2, 1)
g3 = Graph(3, 3)
g10 = Graph(10, 13)

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