from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from queue import PriorityQueue
import heapq

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.my_graph = graph

    def get_graph(self) -> GraphInterface:
        return self.my_graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

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
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
