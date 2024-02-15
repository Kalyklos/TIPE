#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

from math import *

from settings import *
from aeroport import *
from avion import *

def shortest_way (total_way, departure, arrival):
    """fonction déterminant le plus court chemin dans un graph grâce à l'algorithme de Dijkstra

    Args:
        total_way (graph.Graph): Graphe de graph.py dans lequel le chemin le plus court sera chercher.
        departure (str): aéroport de départ.
        arrival (str): aéroport d'arrivé.
    Returns:
        best_way (list): liste des sommets par lesquelles passer.
    """
    pass