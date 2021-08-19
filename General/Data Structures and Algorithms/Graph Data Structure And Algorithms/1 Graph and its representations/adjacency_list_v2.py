"""
A Python program to demonstrate the adjacency list representation of the graph.

This version uses a defaultdict to store the adjacency list.
"""

from collections import defaultdict


class Graph:
    """
    A class to represent a graph. A graph is the list of the adjacency lists.
    Size of the array will be the no. of the vertices "V"
    """

    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        # print(f"self.graph is {self.graph}")

    def add_edge(self, src, dest):
        """
        Function to add an edge in an undirected graph

        :param src:
        :param dest:
        :return:
        """
        # Adding the node to the source node
        self.graph[src].append(dest)

        # Adding the source node to the destination as it is the undirected graph
        self.graph[dest].append(src)

    def print_graph(self):
        """
        Function to print the graph

        :return:
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            for x in temp:
                print(" -> {}".format(x), end="")
            print(" \n")


if __name__ == "__main__":
    """
    Driver program to the above graph class
    """
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
