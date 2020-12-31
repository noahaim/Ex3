import unittest
from src.DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_connected_component_node(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        g.add_edge(0, 5, 5)
        g.add_edge(5, 0, 5)
        g.add_edge(0, 6, 5)
        g.add_edge(6, 0, 5)
        algo = GraphAlgo(g)
        list = algo.connected_component(0)
        for node in list:
            print(node.key)
        g.add_edge(0, 7, 5)
        list = algo.connected_component(0)
        for node in list:
            print(node.key)


if __name__ == '__main__':
    unittest.main()
