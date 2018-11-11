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


    def minPath(self, start, end):
        """
            Dijkstra algorithm
        """
        costs = {start:0}

        nodes = self._nodes.copy()
        path = {}

        next_node = None
        while nodes:
            
            cost_list = [(costs.get(node, float('inf')), node) for node in nodes]
            min_cost, next_node = min(cost_list, key=lambda x:x[0])

            #print(next_node, nodes)

            for neighbour in self._neighbours[next_node]:
                weight = self._edges[(next_node, neighbour)]
                new_cost = weight + costs[next_node]
                if costs.get(neighbour, float('inf')) > new_cost:
                    costs[neighbour] = new_cost
                    path[neighbour] = next_node

            nodes.remove(next_node)
        
        return costs[end],path


    def print(self):
        print('nodes:', self._nodes)
        print('neighbours:', self._neighbours)
        print('edges:', self._edges)


if __name__ == "__main__":
   graph = Graph()

   """    2
       1 ---> 2
       1 ---> 3
          6

          7
       2 ---> 4
       3 ---> 4
          1
   """
   graph.addNodes([1, 2, 3, 4, 5])
   graph.addEdge(1, 2, distance=2)
   graph.addEdge(1, 3, distance=6)
   graph.addEdge(2, 4, distance=7)
   graph.addEdge(3, 4, distance=1)

   min_cost, min_path = graph.minPath(1, 4)
   print("min cost:", min_cost)
   print("min paths:", min_path)

   #graph.print()

        






