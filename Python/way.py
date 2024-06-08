#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8


from math import *
from numpy import *
from random import *
from time import *
#from settings import *
#from aeroport import *
#from avion import *

from collections import defaultdict
import sys

nombre_sommet = 5
 
class Heap():
 
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []
 
    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode
 
    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t
 
    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
 
        if (left < self.size and
           self.array[left][1]
            < self.array[smallest][1]):
            smallest = left
 
        if (right < self.size and
           self.array[right][1]
            < self.array[smallest][1]):
            smallest = right
 
        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:
 
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
 
            # Swap nodes
            self.swapMinHeapNode(smallest, idx)
 
            self.minHeapify(smallest)
 
    # Standard function to extract minimum
    # node from heap
    def extractMin(self):
 
        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return
 
        # Store the root node
        root = self.array[0]
 
        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
 
        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
 
        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)
 
        return root
 
    def isEmpty(self):
        return True if self.size == 0 else False
 
    def decreaseKey(self, v, dist):
 
        # Get the index of v in  heap array
 
        i = self.pos[v]
 
        # Get the node and update its dist value
        self.array[i][1] = dist
 
        # Travel up while the complete tree is
        # not heapified. This is a O(Logn) loop
        while (i > 0 and self.array[i][1] <
                  self.array[(i - 1) // 2][1]):
 
            # Swap this node with its parent
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swapMinHeapNode(i, (i - 1)//2 )
 
            # move to parent index
            i = (i - 1) // 2;
 
    # A utility function to check if a given 
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):
 
        if self.pos[v] < self.size:
            return True
        return False
 
 
def printArr(dist, n):
    print ("Vertex\tDistance from source")
    for i in range(n):
        print ("%d\t\t%d" % (i,dist[i]))
 
 
class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
 
    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):
 
        # Add an edge from src to dest.  A new node 
        # is added to the adjacency list of src. The 
        # node is added at the beginning. The first 
        # element of the node has the destination 
        # and the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)
 
        # Since graph is undirected, add an edge 
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)
 
    # The main function that calculates distances 
    # of shortest paths from src to all vertices. 
    # It is a O(ELogV) function
    def dijkstra(self, src):
 
        V = self.V  # Get the number of vertices in graph
        dist = []   # dist values used to pick minimum 
                    # weight edge in cut
 
        # minHeap represents set E
        minHeap = Heap()
 
        #  Initialize min heap with all vertices. 
        # dist value of all vertices
        for v in range(V):
            dist.append(1e7)
            minHeap.array.append( minHeap.
                                newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)
 
        # Make dist value of src vertex as 0 so 
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])
 
        # Initially size of min heap is equal to V
        minHeap.size = V
 
        # In the following loop, 
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:
 
            # Extract the vertex 
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
 
            # Traverse through all adjacent vertices of 
            # u (the extracted vertex) and update their 
            # distance values
            for pCrawl in self.graph[u]:
 
                v = pCrawl[0]
 
                # If shortest distance to v is not finalized 
                # yet, and distance to v through u is less 
                # than its previously calculated distance
                if (minHeap.isInMinHeap(v) and
                     dist[u] != 1e7 and \
                   pCrawl[1] + dist[u] < dist[v]):
                        dist[v] = pCrawl[1] + dist[u]
 
                        # update distance value 
                        # in min heap also
                        minHeap.decreaseKey(v, dist[v])
 
       # printArr(dist,V)

class Graph_list:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

def taille (graph):
    t = 0
    for i in graph:
        if i[0] > t:
            t = i[0]
        if i[1] > t:
            t = i[1]
    return t+1
totalstart = time()
for i in range (5, 11):
    def BellmanFord(graph, source):
        """Algorithme de Bellman-Ford

        Args:
            graph (Array): tableau de triplet, chacun représentant une arête de la forme (source, destination, taille)
            source (int): Origine du chemin rechercher.

        Returns:
            Array: tableau des distances
        """
        distance = [float("Inf")] * (nombre_sommet+1)
        distance[source] = 0

        for _ in range(nombre_sommet - 1):
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

    print("Temps pour ", nombre_sommet, "sommets")
    def random_graph (p):
        tab_b = []
        g = Graph(nombre_sommet+1)
        gl = Graph_list(nombre_sommet+1)
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range (nombre_sommet):
            gl.add_vertex_data(i, letters[i])
        for i in range (1,nombre_sommet+1):
            for j in range (1, nombre_sommet+1):
                if (i != j):
                    a = random()
                    if a >= p:
                        c = randint(60, 60*8)
                        tab_b.append((i, j, c))
                        tab_b.append((j, i, c))
                        g.addEdge(i, j, c)
                        g.addEdge(j, i, c)
                        gl.add_edge(i, j, c)
        if (not est_connexe(tab_b)):
            return random_graph (p)
        return (tab_b, g, gl)

    def test_des_algo ():
        p = randint(300, 1000)/1000
        graph = random_graph (p)
        return graph

    start = time()
    n = 100000
    graph_alea_b = []
    graph_alea_d = []
    graph_alea_dl = []
    
    for i in range (n):
        a, b, c = test_des_algo()
        graph_alea_b.append(a)
        graph_alea_d.append(b)
        graph_alea_dl.append(c)
    print("Temps de génération aléatoire ", time() - start)

    def test_simulation_speed():
            s1 = time()
            print("starting update")
            for i in range (n):
                BellmanFord (graph_alea_b[i], 1)
            print("graph time Bellman-Ford :", time()-s1)
            s2 = time()
            for i in range (n):
                graph_alea_d[i].dijkstra (1)
            print("graph time Dijkstra heap :", time()-s2)
            s3 = time()
            for i in range (n):
                graph_alea_dl[i].dijkstra('B')
            print("graph time Dijkstra list_adj :", time()-s3)
            
    test_simulation_speed()
    nombre_sommet += 1
print("total:", time()-totalstart)