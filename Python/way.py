#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8


from math import *
from numpy import *
from random import *
from time import *
#from settings import *
#from aeroport import *
#from avion import *

from fibHeap import FibonacciHeap

def dijkstra(adjList, source, sink = None):
    n = len(adjList)    #intentionally 1 more than the number of vertices, keep the 0th entry free for convenience
    visited = [False]*n
    distance = [float('inf')]*n

    heapNodes = [None]*n
    heap = FibonacciHeap()
    for i in range(1, n):
        heapNodes[i] = heap.insert(float('inf'), i)     # distance, label

    distance[source] = 0
    heap.decrease_key(heapNodes[source], 0)

    while heap.total_nodes:
        current = (heap.extract_min()).need_value()
        visited[current] = True

        #early exit
        if sink and current == sink:
            break

        for (neighbor, cost) in adjList[current]:
            if not visited[neighbor]:
                if distance[current] + cost < distance[neighbor]:
                    distance[neighbor] = distance[current] + cost
                    heap.decrease_key(heapNodes[neighbor], distance[neighbor])


    return distance

def taille (graph):
    t = 0
    for i in graph:
        if i[0] > t:
            t = i[0]
        if i[1] > t:
            t = i[1]
    return t+1

def BellmanFord(graph, source):
    """Algorithme de Bellman-Ford

    Args:
        graph (Array): tableau de triplet, chacun représentant une arête de la forme (source, destination, taille)
        source (int): Origine du chemin rechercher.

    Returns:
        Array: tableau des distances
    """
    distance = [float("Inf")] * taille(graph)
    distance[source] = 0

    for _ in range(taille(graph) - 1):
        for u, v, w in graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] != float("Inf") and distance[u] + w < distance[v]:
            print("Graphe avec un cycle négatif")
            return
    del(distance[0])
    return distance

def est_connexe (graph):
    t = BellmanFord(graph, 1)
    for i in t:
        if i == float("Inf"):
            return False
    return True

def random_graph (p):
    tab_b = []
    list_adj = [[],[],[],[],[],[],[]]
    for i in range (1,7):
        for j in range (1, 7):
            a = random()
            if a >= p:
                c = randint(60, 60*8)
                tab_b.append((i, j, c))
                list_adj[i].append((j, c))
    if (not est_connexe(tab_b)):
        return random_graph (p)
    return (tab_b, list_adj)

def test_des_algo ():
    p = randint(300, 500)/1000
    graph = random_graph (p)
    return graph
totalstart = time()
start = time()
n = 50000
graph_alea_b = []
graph_alea_d = []
for i in range (n):
    a, b = test_des_algo()
    graph_alea_b.append(a)
    graph_alea_d.append(b)
print("Temps de génération aléatoire ", time() - start)

def test_simulation_speed():
            s1 = time()
            print("starting update")
            for i in range (n):
                BellmanFord (graph_alea_b[i], 1)
            print("graph time Bellman-Ford :", time()-s1)
            s2 = time()
            for i in range (n):
                dijkstra (graph_alea_d[i], 1)
            print("graph time Bellman-Ford :", time()-s2)
            

test_simulation_speed()
print("total:", time()-totalstart)