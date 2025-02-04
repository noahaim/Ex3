class MyNode:
    def __init__(self, id: int, pos: str = None, tag: int = -1,
                 weight: float = float('inf'), color: str = "White"):
        self.key = id
        if pos is not None and isinstance(pos, str):  # so i can build the node from json when pos is a string
            self.pos = pos.split(",")
            self.pos = [float(i) for i in self.pos]
        else:
            self.pos = pos
        self.__tag = tag
        self.__weight = weight
        self.edges_in = {}
        self.edges_out = {}
        self.__parent = None
        self.__connected_component = None
        self.__color = color

    def get_weight(self):
        return self.__weight

    def get_parent(self):
        return self.__parent

    def get_tag(self):
        return self.__tag

    def get_connected_component(self):
        return self.__connected_component

    def get_key(self):
        return self.key

    def set_color(self, color: str):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_tag(self, tag: int = 0):
        """
            set the tag of the node
            @param:tag
        """
        self.__tag = tag

    def set_connected_component(self, key: int):
        """
            set the SCC for this node
            @param key: The representive node of the SCC
        """
        self.__connected_component = key

    def set_weight(self, weight: float = float('inf')):
        """
            set the weight of this node
            @param: weight
        """
        self.__weight = weight

    def set_parent(self, parent: int = None):
        """
            set the parent of this node
            @param: parent
        """
        self.__parent = parent

    def set_pos(self, other_pos: tuple = None):
        self.pos = other_pos

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
        return self.__weight < other.get_weight()

    def to_dict(self):
        """
        function that return a dict the represent this node
        :return:dict that represent this node
        """
        if self.pos is None:
            return {"id": self.key}
        str_pos = "{},{},{}".format(self.pos[0], self.pos[1], self.pos[2])
        return {"id": self.key, "pos": str_pos}

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

    def __repr__(self):
        return str(self.key) + ": |edges out| " + str(len(self.edges_out)) + " |edges in| " + str(len(self.edges_in))
