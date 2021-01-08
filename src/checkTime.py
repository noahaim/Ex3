import json
import time
import networkx as nx
from src.GraphAlgo import GraphAlgo
from networkx.readwrite import json_graph


class MyCompareTests():
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

    def check_graph(name_file: str):
        print("my graph")
        algo = GraphAlgo()
        start_time = time.perf_counter()
        algo.load_from_json(name_file)
        end_time = time.perf_counter()
        print("load the graph ", end_time - start_time)
        start_time = time.perf_counter()
        print(algo.shortest_path(9, 7))
        end_time = time.perf_counter()
        print("shortest_path ", end_time - start_time)
        start_time = time.perf_counter()
        algo.connected_component(1)
        end_time = time.perf_counter()
        print("connected component ", end_time - start_time)
        start_time = time.perf_counter()
        algo.connected_components()
        end_time = time.perf_counter()
        print("connected_components ", end_time - start_time)
        print(" ")

    def check_graph_nx(name_file):
        print("network x")
        G = MyCompareTests.nx_load_graph(name_file)
        print(G.adj)
        # edges = nx.read_edgelist(name_file)
        # nodes = nx.read_adjlist(name_file)
        # G.add_edges_from(edges)
        # G.add_nodes_from(nodes)
        start_time = time.perf_counter()
        print(nx.nx.dijkstra_path(G,9,7))
        end_time = time.perf_counter()
        print(end_time - start_time)
        start_time = time.perf_counter()
        print(nx.shortest_path(G))
        end_time = time.perf_counter()
        print(end_time - start_time)
        start_time = time.perf_counter()

        end_time = time.perf_counter()
        print(end_time - start_time)


if __name__ == '__main__':
    # MyCompareTests.check_graph("../data/G_30000_240000_0.json")
    # # MyCompareTests.check_graph_nx("../data/G_30000_240000_0.json")
    # MyCompareTests.check_graph("../data/G_20000_160000_0.json")
    # MyCompareTests.check_graph_nx("../data/G_20000_160000_0.json")
    # MyCompareTests.check_graph("../data/G_10000_80000_0.json")
    # MyCompareTests.check_graph_nx("../data/G_10000_80000_0.json")
    # MyCompareTests.check_graph("../data/G_1000_8000_0.json")
    # MyCompareTests.check_graph_nx("../data/G_1000_8000_0.json")
    # MyCompareTests.check_graph("../data/G_100_800_0.json")
    # MyCompareTests.check_graph_nx("../data/G_100_800_0.json")
    MyCompareTests.check_graph("../data/G_10_80_0.json")
    MyCompareTests.check_graph_nx("../data/G_10_80_0.json")
    # G = nx.DiGraph()
    # G.add_edge('a', 'b')
    # G.add_edge('g', 'f')
    # print(dict(nodes=G.nodes(), edges=G.edges()))
