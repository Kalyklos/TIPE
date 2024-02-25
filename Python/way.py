#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

# complexité O(n log(n))

from math import *
from numpy import *

from settings import *
from aeroport import *
from avion import *

def initialisation (reseau, depart):
    """Initialise les distances à + l'infini, nécessaire pour l'algorithme de Dijkstra.

    Args:
        reseau (list): liste des sommets (str) du graphe.
        depart (str): sommet de départ.

    Returns:
        dict : dictionnaire contenant la distance des sommets par rapport à depart, initialiser à l'infini.
    """
    distance = {}
    for sommet in reseau:
        distance[sommet] = inf #on représentera ici l'infini par inf de numpy.
    distance[depart] = 0
    return distance

def with_link (distance):
    """renvoie la liste des sommets référencé et non référencé

    Args:
        distance (dict): dictionnaire renvoyé par initialisation par exemple.

    Returns:
        (list, list): tuple de list contenant les sommets référencés ou non.
    """
    avec = []
    sans = []
    for sommet in distance:
        if distance[sommet] != -1:
            avec.append(sommet)
        else:
            sans.append(sommet)
    return (avec, sans)

def find_min (reseau):
    
    """renvoie le sommet le plus proche parmi les sommets non référencés.

    Args:
        compl (list): list des sommets du graphe (Graph).
    """
    avec, sans = with_link(reseau)
    mini = -1
    plus_proche = "-1"
    for sommet in sans:
        pass

    #ça bug je m'en occuperai plus tard (il faut trouver le sommet de sans le plus proche).
    pass

        

def shortest_way_D (total_way, departure, arrival):
    """fonction déterminant le plus court chemin dans un graph grâce à l'algorithme de Dijkstra

    Args:
        total_way (graph.Graph): Graphe de graph.py dans lequel le chemin le plus court sera chercher.
        departure (str): aéroport de départ.
        arrival (str): aéroport d'arrivé.
    Returns:
        best_way (list): liste des sommets par lesquelles passer.
    """
    pass