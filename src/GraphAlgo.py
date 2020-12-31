from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.my_graph = graph

    def get_graph(self) -> GraphInterface:
        return my_graph


    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.my_graph.get_all_v().get(id1) is None or self.my_graph.get_all_v().get(id2) is None:
            return (float('inf'), [])

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

