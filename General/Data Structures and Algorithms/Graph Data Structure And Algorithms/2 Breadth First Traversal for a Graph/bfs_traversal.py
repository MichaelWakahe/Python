"""
Program to print BFS traversal from a given source vertex. BFS(int s) traverses vertices reachable from s.

This is a modified version of the one found on https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph

It is for a directed graph.
"""

from collections import defaultdict, deque


class Graph:
    """
    This class represents a directed graph using adjacency list representation
    """

    def __init__(self):
        """
        Constructor
        """
        self.graph = defaultdict(list)  # default dictionary to store graph

    def add_edge(self, src, dest):
        """
        Function to add an edge to graph.

        :param src:
        :param dest:
        :return:
        """
        self.graph[src].append(dest)

    def bfs(self, s):
        """
        Function to print a BFS of graph

        :param s:
        :return:
        """
        print(f"graph before starting bfs is {self.graph}")

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        print(f"Initial 'visited' is {visited}\n")

        # Create a queue for BFS
        queue = deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            # print(f"queue before popping: {queue}")
            s = queue.popleft()
            print(s, end=" ")
            # print(f"\nqueue after popping: {queue}")

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                # print(f"\ni is {i}, visited is {visited}")
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


# Driver program to the above graph class
if __name__ == "__main__":

    # Create a graph given in the above diagram
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal starting from vertex 2)")
    g.bfs(2)
