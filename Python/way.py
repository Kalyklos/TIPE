#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8


from math import *
from numpy import *

from settings import *
from aeroport import *
from avion import *

def Dijkstra(graphe, depart):
    """Appelle shortest_way_dijkstra sur graphe.

    Args:
        graphe (dict): Dictionnaire contenant la distance de chaque aéroport par rapport aux autres.
        depart (str or Airport): nom de l'aeroport ou Airport de aeroport.py

    Returns:
        shortest_way_dijkstra sur le graphe avec depart comme aeroport de depart
    """
    return shortest_way_dijkstra ([k.keys for k in graphe], graphe, str(depart))

def shortest_way_dijkstra (sommet, link, depart):
    # complexité O(n log(n))
    """renvoie les distances les plus courtes pour chaque aeroport relativement à l'aeroport de départ grâce à l'algorithme de Dijkstra.

    Args:
        sommet (list): list des sommets du graphe.
        link (dict): dictionnaire de dictionnaire contenant pour chaque aeroport les liens direct avec les aeroports et leur distance (distance par rapport à soit-même = 0).
        depart (str): aeroport de départ.

    Returns:
        dict: dictionnaire contenant la distance à chaque aeroport par rapport à celui de départ.
    """

    # initialisation de toute les distances entre aéroport à l'infini (de numpy).
    distance = {}
    for s in sommet:
        distance[s] = inf
    distance[depart] = 0
    sommet_reference = []
    while [k for k in sommet if distance[k] != inf and k not in sommet_reference] != []: # tant que des sommets sont à l'infini.

        distance_min = inf                                                               # recherche de minimum
        for i in distance:
            if i not in sommet_reference and distance[i] < distance_min:
                distance_min = distance[i]
                indice_sommet = i

        voisins = [k for k in (link[indice_sommet]) if link[indice_sommet][k] != 0]
        for proche in voisins:
            distance[proche] = min(distance[proche], distance[indice_sommet] + link[indice_sommet][proche]) # ajout du plus petit chemin par rapport aux sommets liés.
            sommet_reference.append(indice_sommet)
    return distance