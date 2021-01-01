class MyNode:
    def __init__(self, id: int, pos: tuple = None, tag: int = -1,
                 weight: float = float('inf')):
        self.key = id
        self.pos = pos
        self.tag = tag
        self.weight = weight
        self.edges_in = {}
        self.edges_out = {}
        self.parent = None
        self.connected_component = None

    def set_tag(self, tag: int = 0):
        self.tag = tag

    def set_connected_component(self, key: int):
        self.connected_component = key

    def set_weight(self, weight: float = float('inf')):
        self.weight = weight

    # def get_weight(self, key: int):
    #     return self.weight

    def set_parent(self, parent: int = None):
        self.parent = parent

    def add_edges_in(self, edge_src: int, edge_weight: float):
        self.edges_in[edge_src] = edge_weight

    def add_edges_out(self, edge_dest: int, edge_weight: float):
        self.edges_out[edge_dest] = edge_weight

    def remove_edges_in(self, edge_src: int):
        self.edges_in.__delitem__(edge_src)

    def remove_edges_out(self, edge_dest: int):
        self.edges_out.__delitem__(edge_dest)

    # def __gt__(self, other):
    #     return self.weight < other.weight
    #
    def __eq__(self, other):
        return self.pos == other.pos and self.key == other.key and self.edges_out == other.edges_out \
               and self.edges_in == other.edges_in

    def __lt__(self, other):
        return self.weight < other.weight

    def to_dict(self):
        if self.pos is None:
            return {"id": self.key}
        return {"id": self.key, "pos": self.pos}

    def my_edges(self):
        ans = []
        for dest, w in self.edges_out.items():
            ans.append({"src": self.key, "dest": dest, "w": w})
        return ans
