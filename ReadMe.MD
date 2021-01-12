This project is about developing a data structure of a directional weighted graph.

## We implemented 2 interfaces and 3 class:

### .1.The first class is MyNode:

each node have key ,pos , one dictionary for each edges coming out of him and another dictionary for each edges to him .also he have  parent ,tag  weight,color and connected_component for the algorithm that will do on the graph.
#### The function in this class is:
-set_tag, set_connected_component,set_weight, set_parent ,set_pos.

-add_edges_in , add_edges_out

-remove_edges_in , remove_edges_out

-__eq__-check if 2 nodes are equal by compare their pos and key

-__lt__-compare 2 node by their weight

-to_dict- return a  dictionary that represent this node.

-my_edges-return list of all the edges that coming out of this node.

-__repr__-return string with the node information. 

### 2.The second class is DiGraph implements GraphInterface:
each graph have __mc, __edges_size and dictionary  of __nodes .
####The function in this class is:
-v_size-return the size of nodes in the graph.

-e_size-return the size of the edges in the graph.

-get_all_v- return dictionary  of all the nodes in the graph.

-all_in_edges_of_node-get id of node and return dictionary  of all the edges that is to this node.

-all_out_edges_of_node -get id of node and return dictionary  of all the edges coming out of this node.

-get_mc- return the number of changes made to the graph.

-add_edge , add_node

-remove_edge , remove_node

-to_dict-return a dictionary  that represent this graph.

-from_json-get dictionary  that represent graph and update this graph to be the graph in the dictionary  .

-__eq__-equal between 2 graphs

-__str__-return string with number of edges and number of nodes.

### 3.The third class is GraphAlgo implements GraphAlgoInterface:
this class have field named my_graph that holds a DiGraph.
#### The function in this class is:
-get_graph-return the graph on which the algorithm works in.

-load_from_json-loads a graph from a json file.

-save_to_json-save the graph in json format.

-shortest_path-get 2 nodes and return the weight of the path between them and list of the shortest path using Dijkstra algorithm. Dijkstra algorithm get node src and updates in each node in the graph his weight to be the weight of the shortest path between him and src and his parent to be the node became before him in the shortest path.

-connected_component-get node and return list of the Strongly Connected Component that this node is part of using bfs algorithm. bfs algorithm get src and Boolean that if he is true run the bfs on graph transpose and if false on the original graph. Updates in each node his tag to 0 if there is path from src to him and from him to src.

-connected_components-return list of list of all the Strongly Connected Component in the graph.

-plot_graph-plots the graph.
<a href="https://ibb.co/9wY3QLN"><img src="https://i.ibb.co/KNyzTkX/plot2.png" alt="plot2" border="0"></a>
 
### To clone this repository:
Write in your cmd the following:
```buildoutcfg
$ git clone https://github.com/noahaim/Ex3.git
```

