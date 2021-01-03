import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 0.5)
        g.add_edge(2, 3, 0.3)
        g.add_edge(0, 3, 2)
        g.add_edge(3, 0, 2)
        g.add_edge(3, 4, 6)
        g1 = GraphAlgo(g)
        print(g1.shortest_path(0, 4))
        g1.plot_graph()

    def test_plot(self):
        g = DiGraph()
        g.add_node(0, (2, 3, 4))
        g.add_node(1, (1, 5, 4))
        g.add_node(2)
        g.add_edge(0, 1, 3)
        g.add_edge(1, 2, 3)
        g1 = GraphAlgo(g)
        g1.plot_graph()


if __name__ == '__main__':
    unittest.main()
