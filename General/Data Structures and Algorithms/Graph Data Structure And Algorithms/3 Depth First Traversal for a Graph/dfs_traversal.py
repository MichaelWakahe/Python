"""
Program to print DFS traversal from a given given directed graph.

It is a modified version of the one found at https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
"""
from collections import defaultdict


class Graph:
    """
    This class represents a directed graph using adjacency list representation
    """

    def __init__(self):
        self.graph = defaultdict(list)  # default dictionary to store graph

    def add_edge(self, src, dest):
        """
        Function to add an edge to graph
        """
        self.graph[src].append(dest)

    def dfs_util(self, v, visited):
        """
        A function used by dfs

        :param v:
        :param visited:
        :return:
        """

        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recurse for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        """
        The function to do DFS traversal. It uses recursive dfs_util()

        :param v:
        :return:
        """

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.dfs_util(v, visited)


# Driver code
if __name__ == "__main__":
    # Create a graph given  in the above diagram
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)

    print("\nFollowing is DFS from (starting from vertex 1)")
    g.dfs(1)
