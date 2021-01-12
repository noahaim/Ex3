from GraphInterface import GraphInterface
from MyNode import MyNode


class DiGraph(GraphInterface):
    """This class represents a graph."""

    def __init__(self, other_graph=None):
        if other_graph is None:
            self.__mc = 0
            self.__edges_size = 0
            self.__nodes = {}

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.__nodes)

    def e_size(self) -> int:
        """
            Returns the number of edges in this graph
            @return: The number of edges in this graph
        """
        return self.__edges_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph,
           each node is represented using a pair  (key, node_data)
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
           each node is represented using a pair (key, weight)
        """
        if self.__nodes.get(id1) is None:
            return None
        return self.__nodes.get(id1).edges_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
                weight)
        """
        if self.__nodes.get(id1) is None:
            return None
        return self.__nodes.get(id1).edges_out

    def get_mc(self) -> int:
        """
            Returns the current version of this graph,
            on every change in the graph state - the MC should be increased
            @return: The current version of this graph.
        """
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
            Adds an edge to the graph.
            @param id1: The start node of the edge
            @param id2: The end node of the edge
            @param weight: The weight of the edge
            @return: True if the edge was added successfully, False o.w.

            Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if weight < 0:
            return False
        if id1 == id2:
            return False
        if self.__nodes.get(id1) is None or self.__nodes.get(id2) is None:
            return False
        if self.all_out_edges_of_node(id1).get(id2) is not None:
            return False
        self.__nodes.get(id1).add_edges_out(id2, weight)
        self.__nodes.get(id2).add_edges_in(id1, weight)
        self.__mc += 1
        self.__edges_size += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
            Adds a node to the graph.
            @param node_id: The node ID
            @param pos: The position of the node
            @return: True if the node was added successfully, False o.w.

            Note: if the node id already exists the node will not be added
         """
        if self.__nodes.get(node_id) is None:
            node = MyNode(id=node_id, pos=pos)
            self.__nodes[node_id] = node
            self.__mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
            Removes a node from the graph.
            @param node_id: The node ID
            @return: True if the node was removed successfully, False o.w.

            Note: if the node id does not exists the function will do nothing
         """
        if self.__nodes.get(node_id) is None:
            return False
        for key in self.all_in_edges_of_node(node_id).keys():
            self.__nodes.get(key).remove_edges_out(node_id)
            self.__edges_size -= 1
            self.__mc += 1
        for key in self.all_out_edges_of_node(node_id).keys():
            self.__nodes.get(key).remove_edges_in(node_id)
            self.__edges_size -= 1
            self.__mc += 1
        del self.__nodes[node_id]
        self.__mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
            Removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.

            Note: If such an edge does not exists the function will do nothing
        """
        if self.__nodes.get(node_id1) is None:
            return False
        if self.all_out_edges_of_node(node_id1).get(node_id2) is None:
            return False
        self.__nodes.get(node_id1).remove_edges_out(node_id2)
        self.__nodes.get(node_id2).remove_edges_in(node_id1)
        self.__mc += 1
        self.__edges_size -= 1
        return True

    def to_dict(self):
        """
        :return: return a dict that represent this graph
        """
        ans = {}
        nodes = []
        # for loop that creates list of all the edges in the graph represent as dicts
        for node in self.__nodes.values():
            nodes.append(node.to_dict())
        ans["Nodes"] = nodes
        edges = []
        # for loop that create list of all the edges in the graph represented as dicts
        for node in self.__nodes.values():
            # for each nodes return list of all his edges represent as dicts in list
            for edge in node.my_edges():
                edges.append(edge)
        ans["Edges"] = edges
        return ans

    def from_json(self, json: dict = {}):
        """
            get dict that represent graph and update this graph to be the graph in the dict should be used on empty graph
            :param json: a dict that represent graph
            :return:
        """
        nodes = json["Nodes"]  # list of dicts of nodes
        for node in nodes:
            my_node = MyNode(**node)  # send dict that represent node to the constructor of node
            self.__nodes[my_node.key] = my_node  # add the new node to the graph
        edges = json["Edges"]  # list of dicts of edges
        # for loop that creates the edges in this graph
        for edge in edges:
            self.add_edge(edge.get("src"), edge.get("dest"), edge.get("w"))

    def __eq__(self, other):
        """
            equal between 2 graphs
        :param other:
        :return: return true if 2 graph are equals false otherwise
        """
        if not isinstance(other, self.__class__):
            print(self.__class__)
            print(other.__class__)
            return False
        if self.e_size() != other.e_size() or self.v_size() != other.v_size():
            return False
        return self.get_all_v() == other.get_all_v()  # checks if the nodes are the same (they hold the edges inside
        # so also checks that)

    def __str__(self):
        return "Graph: " + "|V|=" + str(self.v_size()) + " , |E|=" + str(self.e_size())
