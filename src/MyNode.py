from GeoLocation import GeoLocation

class MyNode:
    def __init__(self, key: int, pos: tuple = None, tag: int = 0,
                 weight: float = float('inf')):
        self.key = key
        self.pos = pos
        self.tag = tag
        self.weight = weight
        self.edges_in = {}
        self.edges_out = {}
        self.parent = None

    def set_tag(self, tag: int = 0):
        self.tag = tag

    def set_weight(self, weight: float = float('inf')):
        self.weight = float('inf')

    def set_parent(self, parent: int = None):
        self.parent = parent

    def add_edges_in(self, edge_src: int, edge_weight: float):
        self.edges_in [edge_src] = edge_weight

    def add_edges_out(self, edge_dest: int, edge_weight: float):
        self.edges_out [edge_dest] = edge_weight

    def remove_edges_in(self, edge_src: int):
        self.edges_in.__delitem__(edge_src)

    def remove_edges_out(self, edge_dest: int):
        self.edges_out.__delitem__(edge_dest)
