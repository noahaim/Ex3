import unittest

from DiGraph import DiGraph

class MyTestCase(unittest.TestCase):

    def test_get_mc(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
        self.assertEqual(100, g.get_mc())
        g.remove_node(200)  # doesn't exist should stay 100
        self.assertEqual(100, g.get_mc())
        g.remove_node(50)
        self.assertEqual(101, g.get_mc())
        g.add_edge(0, 5, 5)
        g.add_edge(0, 4, 5)
        g.add_edge(0, 3, 5)
        self.assertEqual(104, g.get_mc())
        g.remove_node(0)
        self.assertEqual(105, g.get_mc())

    def test_v_size(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
        self.assertEqual(100, g.v_size())
        g.remove_node(50)
        self.assertEqual(99, g.v_size())
        g.remove_node(50)  # doesn't exist should stay 99
        self.assertEqual(99, g.v_size())

    def test_e_size(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)

        self.assertEqual(0, g.e_size())
        g.add_edge(0, 5, 5)
        self.assertEqual(1, g.e_size())
        g.add_edge(0, 10, 5)
        self.assertEqual(2, g.e_size())
        g.add_edge(0, 10, 5)  # same edge should stay 2
        self.assertEqual(2, g.e_size())
        g.remove_edge(0, 10)
        self.assertEqual(1, g.e_size())

    def test_add_node(self):
        g = DiGraph()
        g.add_node(50)
        g.add_node(60)
        self.assertEqual(2, g.v_size())
        g.add_node(50)  # already exist
        self.assertEqual(2, g.v_size())

    def test_get_all_v(self):
        g = DiGraph()
        self.assertEqual(0, len(g.get_all_v()))  # No nodes
        for i in range(100):
            g.add_node(i)
        self.assertEqual(100, len(g.get_all_v()))
        self.assertIsNotNone(g.get_all_v().get(0))
        self.assertIsNotNone(g.get_all_v().get(2))
        self.assertIsNone(g.get_all_v().get(1000))

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)

        g.add_edge(0, 20, 10)
        g.add_edge(5, 20, 10)
        self.assertEqual(2, len(g.all_in_edges_of_node(20)))
        g.add_edge(6, 20, 10)
        self.assertEqual(3, len(g.all_in_edges_of_node(20)))
        g.remove_edge(5, 20)
        self.assertEqual(2, len(g.all_in_edges_of_node(20)))
        self.assertIsNotNone(g.all_in_edges_of_node(20).get(6))
        self.assertIsNone(g.all_in_edges_of_node(20).get(700))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)

        g.add_edge(0, 10, 10)
        g.add_edge(0, 20, 10)
        self.assertEqual(2, len(g.all_out_edges_of_node(0)))
        g.add_edge(0, 30, 10)
        self.assertEqual(3, len(g.all_out_edges_of_node(0)))
        self.assertIsNotNone(g.all_out_edges_of_node(0).get(20))
        g.remove_edge(0, 20)
        self.assertIsNone(g.all_out_edges_of_node(0).get(20))
        self.assertEqual(2, len(g.all_out_edges_of_node(0)))
        self.assertIsNotNone(g.all_out_edges_of_node(0).get(10))
        self.assertIsNone(g.all_out_edges_of_node(0).get(900))

    def test_remove_node(self):
        g = DiGraph()
        for i in range(5):
            g.add_node(i)
        self.assertEqual(5, g.v_size())
        g.remove_node(4)
        g.remove_node(6)
        self.assertEqual(4, g.v_size())
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        self.assertEqual(3, g.e_size())
        g.remove_node(1)
        self.assertEqual(1, g.e_size())

    def test_add_edge(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
        g.add_edge(0, 5, 5)
        g.add_edge(0, 6, 6)
        g.add_edge(0, 0, 1)  # no edge between node to himself
        self.assertEqual(2, g.e_size())
        g.add_edge(0, 5, 5)  # adds edge that already exist should stay 2
        self.assertEqual(2, g.e_size())
        self.assertIsNotNone(g.all_out_edges_of_node(0).get(5))
        self.assertIsNone(g.all_out_edges_of_node(0).get(10))  # edge that does not exist
        self.assertIsNotNone(g.all_in_edges_of_node(5).get(0))

    def test_remove_edge(self):
        g = DiGraph()
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2)
        g.add_edge(2, 3, 3)
        g.add_edge(3, 4, 4)
        self.assertEqual(4, g.e_size())
        g.remove_edge(0, 1)
        # the 2 nodes are not un the graph
        g.remove_edge(7, 8)
        # one node in the graph and one not
        g.remove_edge(1, 8)
        g.remove_edge(8, 1)
        # the nodes are in the graph but no edge between them
        g.remove_edge(3, 2)
        self.assertEqual(3, g.e_size())

    def test_equal(self):
        g = DiGraph()
        other = DiGraph()
        self.assertFalse(g == 5)
        self.assertTrue(g == other)
        for i in range(100):
            g.add_node(i)
            other.add_node(i)
        self.assertTrue(g == other)
        g.remove_node(50)
        self.assertFalse(g == other)
        other.remove_node(50)
        self.assertTrue(g == other)
        g.add_edge(0, 2, 2)
        self.assertFalse(g == other)
        other.add_edge(0, 2, 999)
        self.assertFalse(g == other)
        other.remove_edge(0, 2)
        g.remove_edge(0, 2)
        self.assertTrue(g == other)
        self.assertFalse(g == 50)


if __name__ == '__main__':
    unittest.main()
