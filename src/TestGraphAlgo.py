import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


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
        list.sort(lambda x:x.get_key())
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

    def test_plot(self):

        g = DiGraph()
        g.add_node(0, (2, 3, 4))
        g.add_node(1, (1, 5, 4))
        g.add_node(2)
        g.add_edge(0, 1, 3)
        g.add_edge(1, 2, 3)
        g1 = GraphAlgo(g)
        g1.plot_graph()

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
        self.assertTrue(algo.connected_component(0) == algo.connected_component(8))
        self.assertTrue(list.__contains__(g.get_all_v().get(8)))
        # ccs should only contain 9 (no edges from 9)
        list2 = algo.connected_component(9)
        self.assertFalse(list2.__contains__(g.get_all_v().get(8)))
        self.assertTrue(list2.__contains__(g.get_all_v().get(9)))
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

    def test_create(self):
        graph = DiGraph()
        algo = GraphAlgo(graph)
        for i in range(10):
            graph.add_node(i)
        graph.get_all_v().get(0).set_pos((5.2, 5.2, 5.2))
        print(type(graph.get_all_v().get(0).pos[0]))
        algo.save_to_json("test.json")
        algo.load_from_json("test.json")
        print(type(algo.my_graph.get_all_v().get(0).pos[0]))
        print(graph.to_dict())
        algo.load_from_json("A5_edited")
        print(type(algo.my_graph.get_all_v().get(0).pos[0]))
        print((algo.my_graph.get_all_v().get(0).pos[0]))
        print((algo.my_graph.get_all_v().get(0).pos[1]))
        print((algo.my_graph.to_dict()))

    def test_create_graph_1000000_node(self):
        graph = DiGraph()
        for i in range(100000):
            graph.add_node(i)
        for i in range(100):
            for j in range(10):
                graph.add_edge(i, j, 1)
        algo = GraphAlgo(graph)
        algo.save_to_json("graph with 1000000 nodes.json")
        print(graph.e_size())
        print(graph.v_size())

if __name__ == '__main__':
    unittest.main()
