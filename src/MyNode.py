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
        """
            set the tag of the node
            @param:tag
        """
        self.tag = tag

    def set_connected_component(self, key: int):
        """
            set the SCC for this node
            @param key: The representive node of the SCC
        """
        self.connected_component = key

    def set_weight(self, weight: float = float('inf')):
        """
            set the weight of this node
            @param: weight
        """
        self.weight = weight

    def set_parent(self, parent: int = None):
        """
            set the parent of this node
            @param: parent
        """
        self.parent = parent

    def add_edges_in(self, edge_src: int, edge_weight: float):
        """
            get src of  an edge that pointing to this node and it weight
            and add it to a dict edges_in
            @param:edge_src
            @param: edge_weight
        """
        self.edges_in[edge_src] = edge_weight

    def add_edges_out(self, edge_dest: int, edge_weight: float):
        """
            get dest of an edge coming out from this node and its weight
            and add it to dict edges_out
            @param: edge_dest
            @param: edge_weight
        """
        self.edges_out[edge_dest] = edge_weight

    def remove_edges_in(self, edge_src: int):
        """
            get src of edge that point to this node and remove it
            @parm: edge_src
        """
        self.edges_in.__delitem__(edge_src)

    def remove_edges_out(self, edge_dest: int):
        """
             get dest of an edge from this node and remove it
             @parm edge_dest
        """
        self.edges_out.__delitem__(edge_dest)

    def __eq__(self, other):
        """
            checks if 2 nodes are equal return true if they equal false otherwise
        :param other: other node to compare with
        :return: True if they equal else other wise
        """
        # compare their pos,key and list of edges
        if isinstance(other, self.__class__) is False:
            return False
        return self.pos == other.pos and self.key == other.key and self.edges_out == other.edges_out \
            and self.edges_in == other.edges_in

    def __lt__(self, other):
        """
            compare 2 nodes by there weight
            :param other:
            :return: return true if this node weights is smaller the other weight false otherwise
        """
        return self.weight < other.weight

    def to_dict(self):
        """
        function that return a dict the represent this node
        :return:dict that represent this node
        """
        if self.pos is None:
            return {"id": self.key}
        return {"id": self.key, "pos": self.pos}

    def my_edges(self):
        """
        function that return list of all the the edges that coming out of this node
        represent as dict
        :return: list of dicts that represent edges
        """
        ans = []
        for dest, weight in self.edges_out.items():
            ans.append({"src": self.key, "dest": dest, "w": weight})
        return ans
