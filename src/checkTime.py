import time
import json
import time
import networkx as nx
from src.GraphAlgo import GraphAlgo
from src.GraphAlgo import GraphAlgo
from networkx.readwrite import json_graph

avg_python = 0
avg_networkx = 0


class MyCompareTests:

    @classmethod
    def nx_load_graph(cls, name_file: str):
        graph = nx.DiGraph()
        try:
            with open(name_file, "r") as file:
                my_dict = json.load(file)
                # update graph with data inside the dict (add the nodes and the edges)
                nodes_list = my_dict['Nodes']
                edges_list = my_dict['Edges']
                for node in nodes_list:
                    graph.add_node(node['id'])
                for edge in edges_list:
                    graph.add_edge(edge['src'], edge['dest'], weight=edge['w'])
                return graph
        except IOError as e:
            print(e)
            return None

    @classmethod
    def check_graph(cls, name_file: str, src: int, dest: int):
        print("my graph")

        algo = GraphAlgo()
        # start_time = time.perf_counter()
        algo.load_from_json(name_file)
        # end_time = time.perf_counter()
        # print("load the graph ", end_time - start_time)
        # start_time = time.perf_counter()
        # algo.shortest_path(src, dest)
        # end_time = time.perf_counter()
        global avg_python
        # avg_python += end_time - start_time
        # print("shortest_path ", end_time - start_time)
        # start_time = time.perf_counter()
        # algo.connected_component(1)
        # end_time = time.perf_counter()
        # print("connected component ", end_time - start_time)
        start_time = time.perf_counter()
        algo.connected_component(0)
        end_time = time.perf_counter()
        avg_python += end_time - start_time
        # print("connected_components ", end_time - start_time)
        # print(" ")

    @classmethod
    def check_graph_nx(cls, name_file: str, src: int, dest: int):
        print("network x")
        G = MyCompareTests.nx_load_graph(name_file)
        # edges = nx.read_edgelist(name_file)
        # nodes = nx.read_adjlist(name_file)
        # G.add_edges_from(edges)
        # G.add_nodes_from(nodes)
        # start_time = time.perf_counter()
        # nx.shortest_path(G, src, dest)
        # end_time = time.perf_counter()
        global avg_networkx

        # print(end_time - start_time)

        start_time = time.perf_counter()
        nx.strongly_connected_components(G)
        end_time = time.perf_counter()
        avg_networkx += end_time - start_time
        # print(end_time - start_time)
        # print(" ")


if __name__ == '__main__':
    for i in range(100):
            MyCompareTests.check_graph("../data/G_10000_80000_0.json", 50, 70)
    print(avg_python / 100.0, " avg python")
    # print(avg_networkx / 500.0, "avg_nx")


    # MyCompareTests.check_graph_nx("../data/G_20000_160000_0.json", 10, 80)

    # MyCompareTests.check_graph_nx("../data/G_30000_240000_0.json", 8, 90)



    # MyCompareTests.check_graph_nx("../data/G_1000_8000_0.json", 8, 90)

    # MyCompareTests.check_graph_nx("../data/G_100_800_0.json", 9, 70)
    # MyCompareTests.check_graph("../data/G_30000_240000_0.json", 8, 90)

    # G = nx.DiGraph()
    # G.add_edge('a', 'b')
    # G.add_edge('g', 'f')
    # print(dict(nodes=G.nodes(), edges=G.edges()))
    # MyCompareTests.check_graph_nx("../data/G_10_80_0.json", 7, 9)
    # MyCompareTests.check_graph("../data/G_10_80_0.json", 7, 9)
    # MyCompareTests.check_graph("../data/G_100_800_0.json", 9, 70)
    # MyCompareTests.check_graph("../data/G_1000_8000_0.json", 8, 90)

    # MyCompareTests.check_graph("../data/G_20000_160000_0.json", 10, 80)
    # MyCompareTests.check_graph_nx("../data/G_10000_80000_0.json", 50, 70)

