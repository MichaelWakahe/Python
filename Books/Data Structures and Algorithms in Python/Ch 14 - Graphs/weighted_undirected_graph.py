"""
The illustration of this graph is here:
https://www.tutorialspoint.com/data_structures_algorithms/prims_spanning_tree_algorithm.htm

Illustrated below is a Minimum Spanning Tree (MST) of G (G is connected). It uses the Prim-Jarn´ık Algorithm.

Note that minimum spanning trees are only computed for weighted undirected graphs. There should be no self loops or
parallel edges in the graph.

Other algorithms for a minimum spanning tree include Kruskal’s Algorithm.
"""

from collections import defaultdict

from typing import List


class Graph:

    def __init__(self, nodes: list):
        # An adjacency list where for each node the list contains a tuple, the first item in the pair is the neighbour
        # and the second is the weight of the edge
        self.adj_list = defaultdict(List[tuple])
        for node in nodes:
            self.adj_list[node] = []

    def add_edge(self, start, end, weight):
        self.adj_list[start].append((end, weight))
        self.adj_list[end].append((start, weight))

    def get_weight(self, start, end):
        """
        Utility to get the weight of an edge with a start and end node.
        """
        edges = self.adj_list[start]
        for node, weight in edges:
            if node == end:
                return weight

        return float('inf') # Assume there is no edge between the two nodes

    def get_min_node(self, start, mst_set):
        """
        A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in
        the shortest path tree (MST)
        """
        # Initialize the minimum value to a very high number (infinity)
        minimum = 10000     # There is no edge in this graph which has close to this weight, it is considered infinity
        nearest_node = None

        edges = self.adj_list[start]

        for node, weight in edges:
            if node not in mst_set and weight < minimum:
                nearest_node = node
                minimum = weight

        return nearest_node

    def get_min_spanning_tree(self, start):
        """
        This uses Prim-Jarnik Algorithm
        """
        tree = [start]
        unvisited_nodes = set(self.adj_list.keys())
        unvisited_nodes.remove(start)

        while unvisited_nodes:
            next_node = self.get_min_node(tree[-1], set(tree))
            if next_node:
                tree.append(next_node)
                unvisited_nodes.remove(next_node)

        return tree

    def __str__(self):
        descr = ""
        for node in self.adj_list.keys():
            descr = descr + f"Node is {node}, neighbours are: "

            for neighbour in self.adj_list[node]:
                descr = descr + str(neighbour) + ", "

            descr = descr + "\n"

        return descr


if __name__ == "__main__":

    nodes = ['S', 'A', 'B', 'C', 'D', 'T']
    g = Graph(nodes)

    g.add_edge('S', 'A', 7)
    g.add_edge('S', 'C', 8)
    g.add_edge('A', 'C', 3)
    g.add_edge('A', 'B', 6)
    g.add_edge('C', 'B', 4)
    g.add_edge('C', 'D', 3)
    g.add_edge('A', 'D', 3)
    g.add_edge('B', 'D', 2)
    g.add_edge('B', 'T', 5)
    g.add_edge('D', 'T', 2)

    # print(g)

    assert g.get_weight('A', 'B') == 6

    assert g.get_min_node('S', set()) == 'A'
    assert g.get_min_node('B', set()) == 'D'
    assert g.get_min_node('B', set('D')) == 'C'

    print(f"Min spanning tree from S is {g.get_min_spanning_tree('S')}")
