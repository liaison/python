"""
   The Dijkstra algorithm to find the minimal path between two nodes in a graph
   
   Lisong Guo <lisong.guo@me.com>
   Nov 11, 2018
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self._nodes = set()
        self._neighbours = defaultdict(list)
        self._edges = defaultdict(int)

    def addNode(self, new_node):
        self._nodes.add(new_node)

    def addNodes(self, node_list):
        self._nodes.update(node_list)
    
    def addEdge(self, start, end, distance):
        self._neighbours[start].append(end)
        key = (start, end)
        self._edges[key] = distance


    def minpath(self, start, end):
        """
            Dijkstra algorithm
        """
        
        pass

    def print(self):
        print('nodes:', self._nodes)
        print('neighbours:', self._neighbours)
        print('edges:', self._edges)


if __name__ == "__main__":
   graph = Graph()

   """    2
       1 ---> 2
       1 ---> 3
          3

          4
       2 ---> 3
   """
   graph.addNodes([1, 2, 3, 4, 5])
   graph.addEdge(1, 2, distance=2)
   graph.addEdge(1, 3, distance=3)
   graph.addEdge(2, 3, distance=4)

  
   graph.print()

        






