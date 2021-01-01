from GraphInterface import GraphInterface
from MyNode import MyNode


class DiGraph(GraphInterface):

    def __init__(self, other_graph=None):
        if other_graph is None:
            self.__mc = 0
            self.__edges_size = 0
            self.__nodes = {}

    def v_size(self) -> int:
        return len(self.__nodes)

    def e_size(self) -> int:
        return self.__edges_size

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.__nodes.get(id1) is None:
            return None
        return self.__nodes.get(id1).edges_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.__nodes.get(id1) is None:
            return None
        return self.__nodes.get(id1).edges_out

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if weight < 0:
            return False
        if id1 is id2:
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
        if self.__nodes.get(node_id) is None:
            node = MyNode(key=node_id, pos=pos)
            self.__nodes[node_id] = node
            self.__mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if self.__nodes.get(node_id) is None:
            return False
        for key in self.all_in_edges_of_node(node_id).keys():
            self.__nodes.get(key).remove_edges_out(node_id)
            self.__edges_size -= 1
        for key in self.all_out_edges_of_node(node_id).keys():
            self.__nodes.get(key).remove_edges_in(node_id)
            self.__edges_size -= 1
        del self.__nodes[node_id]
        self.__mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.__nodes.get(node_id1) is None:
            return False
        if self.all_out_edges_of_node(node_id1).get(node_id2) is None:
            return False
        self.__nodes.get(node_id1).remove_edges_out(node_id2)
        self.__nodes.get(node_id2).remove_edges_in(node_id1)
        self.__mc += 1
        self.__edges_size -= 1
        return True
