import json
from queue import SimpleQueue
import _json
from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import heapq


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.my_graph = graph

    def get_graph(self) -> GraphInterface:
        return self.my_graph

    def load_from_json(self, file_name: str) -> bool:
        my_dict = {}
        graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                graph.from_json(my_dict)
                self.my_graph = graph
                return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        if self.my_graph is None:
            return False
        try:
            with open(file_name, "w") as file:
                json.dump(self.my_graph, default=lambda m: m.to_dict(), indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def dijkstra(self, src: int):
        # update all th node in the graph to weight inf and parent none
        for node in self.my_graph.get_all_v().values():
            node.set_parent(None)
            node.set_weight(float('inf'))
        # short_path from key to himself is 0
        self.my_graph.get_all_v().get(src).set_weight(0)
        pq_help = []
        heapq.heappush(pq_help, self.my_graph.get_all_v().get(src))
        while pq_help:
            temp_node = heapq.heappop(pq_help)
            for key in self.my_graph.all_out_edges_of_node(temp_node.key).keys():
                m = temp_node.weight + temp_node.edges_out[key]
                if m < self.my_graph.get_all_v().get(key).weight:
                    self.my_graph.get_all_v().get(key).set_weight(m)
                    self.my_graph.get_all_v().get(key).set_parent(temp_node.key)
                    heapq.heappush(pq_help, self.my_graph.get_all_v().get(key))
                    heapq.heapify(pq_help)

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        if self.my_graph.get_all_v().get(id1) is None or self.my_graph.get_all_v().get(id2) is None:
            return float('inf'), []
        self.dijkstra(id1)
        weight_path = self.my_graph.get_all_v().get(id2).weight
        path = [id2]
        parent = self.my_graph.get_all_v().get(id2).parent
        while parent is not None:
            path.append(parent)
            parent = self.my_graph.get_all_v().get(parent).parent
        path.reverse()
        return weight_path, path

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
