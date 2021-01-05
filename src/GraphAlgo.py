import json
from queue import SimpleQueue
import _json
from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import heapq


class GraphAlgo(GraphAlgoInterface):
    """This  class represents an   graphAlgo class."""

    def __init__(self, graph: DiGraph = DiGraph()):
        self.my_graph = graph

    def get_graph(self) -> GraphInterface:
        """
            :return: the directed graph on which the algorithm works on.
         """
        return self.my_graph

    def load_from_json(self, file_name: str) -> bool:
        """
            Loads a graph from a json file.
            @param file_name: The path to the json file
            @returns True if the loading was successful, False o.w.
        """
        graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                # update graph with data inside the dict (add the nodes and the edges)
                graph.from_json(my_dict)
                self.my_graph = graph
                return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
            Saves the graph in JSON format to a file
            @param file_name: The path to the out file
            @return: True if the save was successful, Flase o.w.
        """
        if self.my_graph is None:
            return False
        try:
            with open(file_name, "w") as file:
                # save the graph with the format of to_dict()
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
        """
               Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
               @param id1: The start node id
               @param id2: The end node id
               @return: The distance of the path, the path as a list

               Example:
       #      >>> from GraphAlgo import GraphAlgo
       #       >>> g_algo = GraphAlgo()
       #        >>> g_algo.addNode(0)
       #        >>> g_algo.addNode(1)
       #        >>> g_algo.addNode(2)
       #        >>> g_algo.addEdge(0,1,1)
       #        >>> g_algo.addEdge(1,2,4)
       #        >>> g_algo.shortestPath(0,1)
       #        (1, [0, 1])
       #        >>> g_algo.shortestPath(0,2)
       #        (5, [0, 1, 2])

               More info:
               https://en.wikipedia.org/wiki/Dijkstra's_algorithm
               """

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
        """
            Finds the Strongly Connected Component(SCC) that node id1 is a part of.
            @param id1: The node id
            @return: The list of nodes in the SCC
        """
        # the node is not in the graph
        if self.my_graph.get_all_v().get(id1) is None:
            return []
        # run bfs on graph with id1 as src we the edges as is
        self.bfs(id1, False)
        help_list = []
        # adds all the edges that are reachable from src to a list
        for node in self.my_graph.get_all_v().values():
            if node.tag != -1:
                help_list.append(node)
        # run bfs on graph transpose with id1 as src (read the edges upside down)
        self.bfs(id1, True)
        # if they are still reachable after the edges are flipped its means that its SCC
        help_list = [node for node in help_list if node.tag != -1]  # dealt all of the nodes that are not reachable
        for node in help_list:
            node.set_connected_component(id1)  # update their SCC to src
        return help_list

    def connected_components(self) -> List[list]:
        """
            Finds all the Strongly Connected Component(SCC) in the graph.
            @return: The list all SCC
        """
        # empty graph
        if self.my_graph.v_size() == 0:
            return []
        # reset all the components
        for node in self.my_graph.get_all_v().values():
            node.set_connected_component(None)
        list = []
        # for each node check if its SCC is None is yes  runs connected_components(node)
        # and its SCC  to the list of SCC
        for node in self.my_graph.get_all_v().values():
            if node.connected_component is None:
                list_help = self.connected_component(node.key)
                list.append(list_help)
        return list

    def plot_graph(self) -> None:
        """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
             Otherwise, they will be placed in a random but elegant manner.
            @return: None
        """
        pass

    def bfs(self, node_key: int, upside_down: bool):
        """
        gets src and runs bfs algorithm on the graph from src
        if upside down is true that run the bfs on graph transpose
        :param node_key:
        :param upside_down:
        :return:
        """
        # initialize all the tags to -1
        for node in self.my_graph.get_all_v().values():
            node.set_tag(-1)
        queue = SimpleQueue()
        src = self.my_graph.get_all_v().get(node_key)
        src.set_tag(0)
        queue.put(src)
        while not queue.empty():
            node_temp = queue.get()
            # graph as is
            if upside_down is False:
                neighbors = self.my_graph.all_out_edges_of_node(node_temp.key)
            # graph transpose
            else:
                neighbors = self.my_graph.all_in_edges_of_node(node_temp.key)
            for key in neighbors:
                node_neighbor = self.my_graph.get_all_v().get(key)
                if node_neighbor.tag == -1:  # the first time this node is reached
                    node_neighbor.set_tag(node_temp.tag + 1)
                    queue.put(node_neighbor)
