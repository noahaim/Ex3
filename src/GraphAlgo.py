from queue import SimpleQueue
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.my_graph = graph

    def get_graph(self) -> GraphInterface:
        return self.my_graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        if self.my_graph.get_all_v().get(id1) is None or self.my_graph.get_all_v().get(id2) is None:
            return float('inf'), []

    def connected_component(self, id1: int) -> list:
        if self.my_graph.get_all_v().get(id1) is None:
            return []
        self.bfs(id1, False)
        help_list = []
        for node in self.my_graph.get_all_v().values():
            if node.tag != -1:
                help_list.append(node)
        self.bfs(id1, True)
        help_list = [node for node in help_list if node.tag != -1]
        for node in help_list:
            node.set_connected_component(id1)
        return help_list

    def connected_components(self) -> List[list]:
        if self.my_graph.v_size() == 0:
            return []
        for node in self.my_graph.get_all_v().values():
            node.set_connected_component(None)
        list = []
        for node in self.my_graph.get_all_v().values():
            if node.connected_component is None:
                list_help = self.connected_component(node.key)
                list.append(list_help)
        return list

    def plot_graph(self) -> None:
        pass

    def bfs(self, node_key: int, upside_down: bool):
        for node in self.my_graph.get_all_v().values():
            node.set_tag(-1)

        queue = SimpleQueue()
        src = self.my_graph.get_all_v().get(node_key)
        src.set_tag(0)
        queue.put(src)
        while not queue.empty():
            node_temp = queue.get()
            if upside_down is False:
                neighbors = self.my_graph.all_out_edges_of_node(node_temp.key)
            else:
                neighbors = self.my_graph.all_in_edges_of_node(node_temp.key)
            for key in neighbors:
                node_neighbor = self.my_graph.get_all_v().get(key)
                if node_neighbor.tag == -1:
                    node_neighbor.set_tag(node_temp.tag + 1)
                    queue.put(node_neighbor)
