import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(5):
            g.add_node(i)
        g1 = GraphAlgo(g)
        self.assertEqual((float('inf'), []), g1.shortest_path(0, 4))
        self.assertEqual((float('inf'), []), g1.shortest_path(8, 9))
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 0.5)
        g.add_edge(2, 3, 0.3)
        g.add_edge(0, 3, 2)
        g.add_edge(3, 0, 2)
        g.add_edge(3, 4, 6)
        self.assertEqual((7.8, [0, 1, 2, 3, 4]), g1.shortest_path(0, 4))
        self.assertEqual((float('inf'), []), g1.shortest_path(6, 0))

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
        self.assertTrue(list.__contains__(g.get_all_v().get(5).get_key()))
        self.assertTrue(list.__contains__(g.get_all_v().get(6).get_key()))
        # add 7 but only one sided
        g.add_edge(0, 7, 5)
        list = algo.connected_component(0)
        self.assertFalse(list.__contains__(g.get_all_v().get(7)))
        # add 8 to the the ccs of 0
        g.add_edge(6, 8, 8)
        g.add_edge(8, 6, 8)
        list = algo.connected_component(0)
        list8 = algo.connected_component(8)
        list.sort()
        list8.sort()
        self.assertTrue(list == list8)
        self.assertTrue(list.__contains__(g.get_all_v().get(8).get_key()))
        # ccs should only contain 9 (no edges from 9)
        list2 = algo.connected_component(9)
        self.assertFalse(list2.__contains__(g.get_all_v().get(8).get_key()))
        self.assertTrue(list2.__contains__(g.get_all_v().get(9).get_key()))
        # creating list for the ccs of 5 should be equal to the list of node 0 because its the same ccs
        list3 = algo.connected_component(5)
        for node in list3:
            self.assertTrue(list.__contains__(node))

    def test_list_of_SCC(self):
        g = DiGraph()

        for i in range(5):
            g.add_node(i)
        algo = GraphAlgo(g)
        self.assertEqual(5, len(algo.connected_components()))
        self.assertTrue(algo.connected_components().__contains__(algo.connected_component(4)))
        g.add_edge(0, 1, 1)
        self.assertEqual(5, len(algo.connected_components()))
        g.add_edge(1, 0, 1)  # SCC with 0 and 1
        self.assertEqual(4, len(algo.connected_components()))
        self.assertTrue(algo.connected_components().__contains__(algo.connected_component(0)))
        g.add_edge(1, 2, 0)
        self.assertEqual(4, len(algo.connected_components()))
        g.add_edge(2, 0, 0)
        self.assertEqual(3, len(algo.connected_components()))
        g.remove_edge(2, 0)
        self.assertEqual(4, len(algo.connected_components()))
        g.add_edge(2, 0, 0)
        self.assertTrue(algo.connected_components().__contains__(algo.connected_component(2)))

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
        self.assertFalse(graph is graph_algo.get_graph())
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
        graph.remove_node(0)
        graph.remove_node(5)
        graph.remove_edge(3, 5)
        self.assertFalse(graph == graph_algo.get_graph())
        # empty graph test
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        self.assertTrue(graph_algo.save_to_json("json_test.json"))
        self.assertTrue(graph_algo.load_from_json("json_test.json"))
        self.assertTrue(graph == graph_algo.get_graph())

    def test_plot(self):

        g = DiGraph()
        g.add_node(0, (1, 1, 4))
        g.add_node(1, (2, 2, 4))
        g.add_node(2, (3, 3, 3))
        g.add_node(3, (4, 4, 4))
        g.add_node(4, (5, 5, 5))
        g.add_node(5, (6, 6, 6))
        g.add_node(6, (7, 6, 7))
        g.add_node(7, (8, 5, 5))
        g.add_node(8, (9, 4, 4))
        g.add_node(9, (10, 3, 3))
        g.add_node(10, (14, 16, 1))
        g.add_node(11, (8, 16, 1))
        g.add_node(12, (9, 14, 1))
        g.add_node(13, (10, 10, 1))
        g.add_node(14)
        g.add_node(15)
        g.add_edge(0, 1, 3)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 5, 3)
        g.add_edge(5, 6, 3)
        g.add_edge(6, 7, 3)
        g.add_edge(7, 8, 3)
        g.add_edge(8, 9, 3)
        g.add_edge(9, 0, 3)
        g.add_edge(10, 11, 3)
        g.add_edge(11, 12, 3)
        g.add_edge(12, 13, 3)
        g.add_edge(13, 14, 3)
        g.add_edge(14, 15, 3)
        g1 = GraphAlgo(g)
        g1.plot_graph()

if __name__ == '__main__':
    unittest.main()
