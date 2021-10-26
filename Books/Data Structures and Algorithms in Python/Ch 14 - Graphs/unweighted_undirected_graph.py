"""
A graph representing the flight connections between the cities mentioned in this chapter.

In this representation, there is a link between the cities without mentioning the distance. The link is bidirectional
(undirected). There are no self loops in the graph.

It represents the graph with an Adjacency List.

The following are explored in this module:
1) Visit all the nodes using a Breadth First Search (BFS) approach
2) Visit all the nodes using a Depth First Search (DFS) approach
3) Decide on the reachability of a node (which can be achieved by modifying slightly either (1) or (2)
4) Detect a cycle
5) Computing the shortest path from vertex u to vertex v, or reporting that no such path exists.
Not yet done:
6) Testing whether G is connected. A graph is connected if, for any two vertices, there is a path between them.
7) Computing a (minimum) spanning tree of G, if G is connected.

"""

from entities import City

from collections import defaultdict, deque
from typing import List


class Graph:
    def __init__(self, cities: List[City] = []):
        self.adj_list = defaultdict(list)
        for city in cities:
            self.adj_list[city] = []

    def add_edge(self, source: City, dest: City):
        self.adj_list[source].append(dest)
        self.adj_list[dest].append(source)

    def bfs_traverse(self, c: City):
        """
        c: the city at which to start the traversal
        """
        queue = deque()
        visited = set()

        queue.append(c)
        visited.add(c.name)     # the city name is considered unique

        while queue:
            city = queue.popleft()
            print(f"Have visited {city.name}")

            for neighbour in self.adj_list[city]:
                if neighbour.name not in visited:
                    visited.add(neighbour.name)     # the city name is considered unique
                    queue.append(neighbour)

    def dfs_traverse(self, city: City, visited: set = set()):
        """
        city: the city at which to start the traversal
        """
        if city.name not in visited:
            print(f"Visiting {city.name}")
            visited.add(city.name)

            for neighbour in self.adj_list[city]:
                self.dfs_traverse(neighbour, visited)

    def detect_cycle(self, city: City, visited: set, parent: City):
        """
        The existence of a cycle in directed and undirected graphs can be determined by whether depth-first search (DFS)
        finds an edge that points to an ancestor of the current vertex (it contains a back edge).  In an undirected
        graph, the edge to the parent of a node should not be counted as a back edge, but finding any other already
        visited vertex will indicate a back edge.
        """
        # Mark the current node as visited
        visited.add(city.name)
        # print(f"v is {v}, parent is {parent}, visited is {visited}")

        # Recurse for all the vertices adjacent to this vertex
        for c in self.adj_list[city]:

            # If the node is not visited then recurse on it
            if c.name not in visited:
                if self.detect_cycle(c, visited, city):
                    return True

            # If an adjacent vertex is visited and not a parent of current city, then there is a cycle
            elif parent != c:
                return True

        return False

    def find_shortest_path(self, start: City, end: City):
        """
        Shortest path with an unweighted graph is calculated using BFS.
        """
        queue = deque()
        visited = set()

        dist_hash = {}
        parent_hash = {}

        queue.append(start)
        visited.add(start.name)  # the city name is considered unique

        dist_hash[start.name] = 0

        while queue:
            city = queue.popleft()
            # print(f"Have visited {city.name}")

            for neighbour in self.adj_list[city]:
                if neighbour.name not in visited:
                    visited.add(neighbour.name)  # the city name is considered unique
                    queue.append(neighbour)
                    dist_hash[neighbour.name] = dist_hash[city.name] + 1
                    parent_hash[neighbour.name] = city.name

        # for key in dist_hash.keys():
        #     print(f"key is {key}, value is {dist_hash[key]}")
        #
        # print("")
        #
        # for key in parent_hash.keys():
        #     print(f"key is {key}, value is {parent_hash[key]}")

        # Construct the shortest path by starting at the end point and working backwards.
        dest = end.name
        shortest_path = [dest]
        prev = dest
        while prev != start.name:
            prev = parent_hash[prev]
            shortest_path.append(prev)

        shortest_path.reverse()

        return dist_hash[end.name], shortest_path

    def __str__(self):
        descr = ""

        for city in self.adj_list.keys():
            descr = descr + f"city is {city.name}, connections are: "

            for adj_city in self.adj_list[city]:
                descr = descr + str(adj_city.name) + ", "

            descr = descr + "\n"

        return descr


if __name__ == "__main__":

    city_bos = City("BOS")
    city_ord = City("ORD")
    city_sfo = City("SFO")
    city_lax = City("LAX")
    city_dfw = City("DFW")
    city_mia = City("MIA")
    city_jfk = City("JFK")

    cities = [city_bos, city_ord, city_sfo, city_lax, city_dfw, city_mia, city_jfk]
    g = Graph(cities)

    # This represents 14.2 (page 622) but without directions and weights
    g.add_edge(city_bos, city_jfk)
    g.add_edge(city_bos, city_mia)
    g.add_edge(city_jfk, city_sfo)
    g.add_edge(city_jfk, city_mia)
    g.add_edge(city_ord, city_dfw)
    g.add_edge(city_ord, city_lax)
    g.add_edge(city_lax, city_dfw)
    g.add_edge(city_lax, city_mia)
    g.add_edge(city_dfw, city_mia)

    # print(f"graph is:\n{g}")

    # print("A BFS Traversal:")
    # g.bfs_traverse(city_bos)

    # print("A DFS Traversal:")
    # g.dfs_traverse(city_bos)

    print(f"Cycle detected at {city_sfo.name}: {g.detect_cycle(city_sfo, set(), city_sfo)}")

    # print(f"Shortest path is {g.find_shortest_path(city_bos, city_lax)}")
    # print(f"Shortest path is {g.find_shortest_path(city_bos, city_ord)}")
