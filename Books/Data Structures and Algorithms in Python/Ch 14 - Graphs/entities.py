"""
To capture various forms of nodes and edges.
"""


class City:
    """
    This is representative of a city in a flight path.
    """

    def __init__(self, name: str = None, city_id: int = 0):
        """
        The city_id is meant to be a unique number representing a city. The ids should be consecutive, starting at zero.
        This allows for an Adjacency Matrix to be constructed with the cities.
        """
        self.name = name
        self.city_id = city_id

    def __str__(self):
        return "Name is " + self.name + ", city id is " + str(self.city_id)

    def __hash__(self):
        """
        This assumes no two cities have the same name.
        """
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, City):
            return self.name == other.name

        return False
