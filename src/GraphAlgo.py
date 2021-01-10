import json
import math
import random
from queue import SimpleQueue, PriorityQueue
from typing import List

import matplotlib.pyplot as plt

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


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
        """
        get node src and updates the weight of each node in the graph to the weight of the shortest path from it to src
        and also updates in each node his parent on the shortest path
        :param src:
        """
        # update all th node in the graph to weight inf and parent none
        for node in self.my_graph.get_all_v().values():
            node.set_parent(None)
            node.set_weight(float('inf'))
        # short_path from key to himself is 0
        start = self.my_graph.get_all_v().get(src)
        start.set_weight(0)
        # creates priority queue and insert src node
        pq_help = PriorityQueue()
        pq_help.put((start.get_weight(), start))
        while pq_help.qsize() != 0:
            # removes the node with the smallest weight from priority queue
            temp_node = pq_help.get()[1]
            # go over his all neighbors
            for key in self.my_graph.all_out_edges_of_node(temp_node.key).keys():
                # calculate the weight of temp_node and with the edge between him and the neighbor
                m = temp_node.get_weight() + temp_node.edges_out[key]
                # if this weight is less than the neighbor's weight update the parent and the neighbor's weight and
                # insert it to the priority queue
                node = self.my_graph.get_all_v().get(key)
                if m < node.get_weight():
                    node.set_weight(m)
                    node.set_parent(temp_node.key)
                    pq_help.put((node.get_weight(), node))

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        """
        node2 = self.my_graph.get_all_v().get(id2)
        # id id1 or id2 not in the graph
        if self.my_graph.get_all_v().get(id1) is None or node2 is None:
            return float('inf'), []
        #  Updates the weight of each node to the weight of the shortest path from it to id1 and his parent
        self.dijkstra(id1)
        #  the weight of the shortest path from id1 to id2
        weight_path = node2.get_weight()
        #  no path from id1 to id2
        if weight_path is float('inf'):
            return float('inf'), []
        path = [id2]
        parent = node2.get_parent()
        # Get the short path by the parents
        while parent is not None:
            path.append(parent)
            parent = self.my_graph.get_all_v().get(parent).get_parent()
        # The path is from the end to the beginning so we will reverse it
        path.reverse()
        return weight_path, path

    def connected_component(self, id1: int) -> list:
        """
            Finds the Strongly Connected Component(SCC) that node id1 is a part of.
            @param id1: The node id
            @return: The list of nodes in the SCC
        """
        if self.my_graph is None:
            return []
        # the node is not in the graph
        if self.my_graph.get_all_v().get(id1) is None:
            return []
        # run bfs on graph with id1 as src we the edges as is
        self.bfs(id1, False)
        help_list = []
        # adds all the edges that are reachable from src to a list
        for node in self.my_graph.get_all_v().values():
            if node.get_tag() != -1:
                help_list.append(node)
        # run bfs on graph transpose with id1 as src (read the edges upside down)
        self.bfs(id1, True)
        # if they are still reachable after the edges are flipped its means that its SCC
        help_list = [node for node in help_list if node.get_tag() != -1]  # dealt all of the nodes that are not reachable
        for node in help_list:
            node.set_connected_component(id1)  # update their SCC to src
        help_list = [node.get_key() for node in help_list]
        return help_list

    def connected_components(self) -> List[list]:
        """
            Finds all the Strongly Connected Component(SCC) in the graph.
            @return: The list all SCC
        """
        if self.my_graph is None:
            return []
        # empty graph
        if self.my_graph.v_size() == 0:
            return []
        # reset all the components
        for node in self.my_graph.get_all_v().values():
            node.set_connected_component(None)
            node.set_color("Red")
        list = []
        # for each node check if its SCC is None is yes  runs connected_components(node)
        # and its SCC  to the list of SCC
        for node in self.my_graph.get_all_v().values():
            if node.get_connected_component() is None:
                list_help = self.connected_component(node.key)
                list.append(list_help)
        for node in self.my_graph.get_all_v().values():
            node.set_color("White")
        return list

    def plot_graph(self) -> None:

        """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
             Otherwise, they will be placed in a random but elegant manner.
            @return: None
        """
        x_vals = []
        y_vals = []
        for v in self.my_graph.get_all_v().values():
            if v.pos is None:
                v.set_pos((random.random() * 100, random.random() * 100, 0))
            x_vals.append(v.pos[0])
            y_vals.append(v.pos[1])
        # ax = plt.axes()
        for v in self.my_graph.get_all_v().values():
            plt.annotate(v.key, (v.pos[0], v.pos[1]), fontsize=10)
            for n in self.my_graph.all_out_edges_of_node(v.key).keys():
                x1 = v.pos[0]
                y1 = v.pos[1]
                x2 = self.my_graph.get_all_v().get(n).pos[0]
                y2 = self.my_graph.get_all_v().get(n).pos[1]
                plt.annotate(text="", xy=(x1, y1), xytext=(x2, y2),arrowprops=dict(arrowstyle="<|-"))
        plt.scatter(x_vals, y_vals, s=50)
        plt.show()

    # def dfs_node(self, transpose: bool, time: int, node):
    #     my_stack = stack()
    #     my_stack.put(node)
    #     while not my_stack.empty():
    #         my_node = my_stack.get()
    #         if my_node.get_color()== "White":
    #             my_node.set_color("Gray")
    #             my_time = time + 1
    #             node.set_tag(time)
    #             if transpose is False:
    #                 neighbors = self.my_graph.all_out_edges_of_node(node.key)
    #             else:
    #                 neighbors = self.my_graph.all_in_edges_of_node(node.key)
    #             for key in neighbors:
    #              node_neighbor = self.my_graph.get_all_v().get(key)
    #             if node_neighbor.get_color == "White":
    #                 node_neighbor.set_parent(my_node)
    #                 my_stack.put(node_neighbor)

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
            if node.get_color != "Red" or node.connected_component is None:
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

                if node_neighbor.get_tag() == -1:  # the first time this node is reached
                    node_neighbor.set_tag(0)
                    queue.put(node_neighbor)
