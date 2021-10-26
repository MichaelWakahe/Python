"""
A graph representing the flight connections between the cities mentioned in this chapter.

In this representation, there is a link between the cities together with the distance. The links are directional (the
graph is a directed graph or digraph). There are no self loops in the graph.

It represents the graph with an Adjacency Matrix.

The following are explored in this module:
1) The shortest path between two cities

Not yet done:
Computing a directed path from vertex u to vertex v, or reporting that no such
path exists.

• Finding all the vertices of the graph that are reachable from a given vertex s.
• Determine whether the graph is acyclic.
• Determine whether the graph is strongly connected.
Transitive closure (see section 14.4)

"""

from entities import City

from collections import deque


class Graph:

    def __init__(self, num_cities: int = 0):
        """
        num_cities: the number of cities (nodes)
        """
        self.num_cities = num_cities
        self.adj_matrix = [[-1 for x in range(num_cities)] for x in range(num_cities)]
        self.city_hash = {}     # A hashmap of all cities, where the key is the city_id and the value is the name

    def add_city(self, city: City):
        self.city_hash[city.city_id] = city.name

    def add_flight_path(self, source: City, dest: City, distance: int):
        self.adj_matrix[source.city_id][dest.city_id] = distance

    def get_neighbours(self, city: City) -> list:
        distances = self.adj_matrix[city.city_id]
        neighbours = []

        for j in range(self.num_cities):
            if distances[j] > 0:
                neighbours.append(City(self.city_hash[j], j))

        return neighbours

    def find_shortest_path(self, start: City, end: City):
        """
        An implementation of Dijkstra’s Algorithm.
        """
        shortest_distance = float('inf')
        parent_hash = {}    # To track the path that it went through

        distances = {}
        for city_id in self.city_hash.keys():
            distances[self.city_hash[city_id]] = float('inf')
        distances[start.name] = 0

        queue = deque()   # To be used for the BFS
        queue.append(start.city_id)

        visited = set()     # Keep a track of visited cities using their name (which is unique)

        while queue:
            city_id = queue.popleft()
            city_name = self.city_hash[city_id]
            visited.add(city_name)

            for neighbour in self.get_neighbours(City(city_name, city_id)):     # A cleaner implementation needed
                if neighbour.name not in visited:
                    if distances[neighbour.name] > distances[city_name] + self.adj_matrix[city_id][neighbour.city_id]:
                        distances[neighbour.name] = distances[city_name] + self.adj_matrix[city_id][neighbour.city_id]
                        parent_hash[neighbour.name] = city_name

                    if neighbour == end:
                        shortest_distance = distances[neighbour.name]
                        break
                    else:
                        queue.append(neighbour.city_id)

        # print(parent_hash)
        # Work our way backwards using the parent_hash in order to get the path
        path = []
        if shortest_distance != float('inf'):
            parent_city = ""
            path.append(end.name)
            while parent_city != start.name:
                parent_city = parent_hash[path[len(path) - 1]]
                path.append(parent_city)
        path.reverse()

        return shortest_distance, path

    def __str__(self):
        descr = "Cities are (name, city_id): "

        for city_id in self.city_hash.keys():
            descr = descr + f"({self.city_hash[city_id]},{city_id}); "

        descr = descr + "\n"

        # A list of edges has not been added to the description.
        return descr

    def get_matrix(self):
        return self.adj_matrix


if __name__ == "__main__":
    g = Graph(7)

    city_bos = City("BOS", 0)
    city_ord = City("ORD", 1)
    city_sfo = City("SFO", 2)
    city_lax = City("LAX", 3)
    city_dfw = City("DFW", 4)
    city_mia = City("MIA", 5)
    city_jfk = City("JFK", 6)

    g.add_city(city_bos)
    g.add_city(city_ord)
    g.add_city(city_sfo)
    g.add_city(city_lax)
    g.add_city(city_dfw)
    g.add_city(city_mia)
    g.add_city(city_jfk)

    # For the distance between cities, refer to Figure 14.2 (page 622). I remove the first two letters of the flight
    # path name and use the numbers associated. There are 11 flights (edges).
    g.add_flight_path(city_bos, city_jfk, 35)
    g.add_flight_path(city_bos, city_mia, 247)
    g.add_flight_path(city_jfk, city_sfo, 45)
    g.add_flight_path(city_jfk, city_mia, 903)
    g.add_flight_path(city_jfk, city_dfw, 1387)
    g.add_flight_path(city_mia, city_dfw, 523)
    g.add_flight_path(city_mia, city_lax, 411)
    g.add_flight_path(city_dfw, city_lax, 49)
    g.add_flight_path(city_dfw, city_ord, 335)
    g.add_flight_path(city_ord, city_dfw, 877)
    g.add_flight_path(city_lax, city_ord, 120)

    # print(g)
    # print(g.get_matrix())

    # print(f"Neighbours of {city_bos.name} are {g.get_neighbours(city_bos)}")

    print(f"Shortest path is {g.find_shortest_path(city_bos, city_lax)}")
    print(f"Shortest path is {g.find_shortest_path(city_bos, city_ord)}")
    print(f"Shortest path is {g.find_shortest_path(city_lax, city_sfo)}")