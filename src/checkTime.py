import time

from src.GraphAlgo import GraphAlgo
class checkTime:

    def check_graph(name_file):

        algo = GraphAlgo()
        start_time = time.perf_counter()
        algo.load_from_json(name_file)
        end_time = time.perf_counter()
        print("load the graph ", end_time - start_time)
        start_time = time.perf_counter()
        algo.shortest_path(0, 79)
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

if __name__ == '__main__':
    checkTime.check_graph("../data/G_30000_240000_0.json")
    checkTime.check_graph("../data/G_20000_160000_0.json")
    checkTime.check_graph("../data/G_10000_80000_0.json")
    checkTime.check_graph("../data/G_1000_8000_0.json")
    checkTime.check_graph("../data/G_100_800_0.json")
    checkTime.check_graph("../data/G_10_80_0.json")
