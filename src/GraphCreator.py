import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo



class MyTestCase(unittest.TestCase):
    def test_create_graph_1000000_node(self):
        graph = DiGraph()
        for i in range(1000001):
            graph.add_node(i)
        for i in range(1000001):
            for j in range(10):
                graph.add_edge(i, j, 1)
        algo = GraphAlgo(graph)
        algo.save_to_json("graph with 1000000 nodes.json")


if __name__ == '__main__':
    unittest.main()
