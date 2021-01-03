import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_connected_component_node(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)

        # creating ccs between 0,5,6
        g.add_edge(0, 5, 5)
        g.add_edge(5, 0, 5)
        g.add_edge(0, 6, 5)
        g.add_edge(6, 0, 5)
        algo = GraphAlgo(g)
        list = algo.connected_component(0)
        self.assertTrue(list.__contains__(g.get_all_v().get(5)))
        self.assertTrue(list.__contains__(g.get_all_v().get(6)))
        # add 7 but only one sided
        g.add_edge(0, 7, 5)
        list = algo.connected_component(0)
        self.assertFalse(list.__contains__(g.get_all_v().get(7)))
        # add 8 to the the ccs of 0
        g.add_edge(6, 8, 8)
        g.add_edge(8, 6, 8)
        list = algo.connected_component(0)
        self.assertTrue(list.__contains__(g.get_all_v().get(8)))
        # ccs should only contain 9 (no edges from 9)
        list2 = algo.connected_component(9)
        self.assertFalse(list2.__contains__(g.get_all_v().get(8)))
        self.assertTrue(list2.__contains__(g.get_all_v().get(9)))
        # creating list for the ccs of 5 should be equal to the list of node 0 because its the same ccs
        list3 = algo.connected_component(5)
        for node in list3:
            self.assertTrue(list.__contains__(node))

    def test_json_save_and_lode(self):
        # simple graph no edges
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        for i in range(100):
            graph.add_node(i)
        self.assertTrue(graph_algo.save_to_json("json_test.json"))
        self.assertTrue(graph_algo.load_from_json("json_test.json"))
        self.assertTrue(graph == graph_algo.get_graph())
        graph.remove_node(50)
        self.assertFalse(graph == graph_algo.get_graph())
        # big graph with edges
        graph = DiGraph()
        for i in range(1000):
            graph.add_node(i)
        for i in range(1000):
            graph.add_edge(i, 0, 5)
            graph.add_edge(i, 2, 5)
            graph.add_edge(i, 3, 5)
        graph_algo = GraphAlgo(graph)
        self.assertTrue(graph_algo.save_to_json("json_test.json"))
        self.assertTrue(graph_algo.load_from_json("json_test.json"))
        self.assertTrue(graph == graph_algo.get_graph())
        # empty graph test
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        self.assertTrue(graph_algo.save_to_json("json_test.json"))
        self.assertTrue(graph_algo.load_from_json("json_test.json"))
        self.assertTrue(graph == graph_algo.get_graph())


if __name__ == '__main__':
    unittest.main()
