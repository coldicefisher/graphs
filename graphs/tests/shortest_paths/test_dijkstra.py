# # tests/shortest_paths/test_dijkstra.py

# import pytest
# from graphs.core.graph import Graph
# from graphs.shortest_paths.dijkstra import dijkstra
# from graphs.utils import make_node_path_from_last


# 
# # Helper Graph Builders
# 

# def make_weighted_graph():
#     #      (1)
#     # 0 -------- 1
#     #  \        /
#     #   \ (4)  (2)
#     #    \    /
#     #      2
#     #
#     g = Graph(3, undirected=True)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(1, 2, 2.0)
#     g.insert_edge(0, 2, 4.0)
#     return g


# def make_chain_graph():
#     # 0 -> 1 -> 2 -> 3
#     g = Graph(4)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(1, 2, 1.0)
#     g.insert_edge(2, 3, 1.0)
#     return g


# def make_disconnected_graph():
#     g = Graph(4, undirected=True)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(2, 3, 1.0)
#     return g


# 
# # Basic Shortest Path Tests
# 

# def test_dijkstra_simple_graph():
#     g = make_weighted_graph()

#     dist, last = dijkstra(g, 0)

#     # Expected shortest distances
#     assert dist[0] == 0
#     assert dist[1] == 1
#     assert dist[2] == 3  # via 1

#     path = make_node_path_from_last(last, 2)
#     assert path == [0, 1, 2]


# def test_dijkstra_chain_graph():
#     g = make_chain_graph()

#     dist, last = dijkstra(g, 0)

#     assert dist == [0, 1, 2, 3]

#     path = make_node_path_from_last(last, 3)
#     assert path == [0, 1, 2, 3]


# 
# # Unreachable Nodes
# 

# def test_dijkstra_disconnected():
#     g = make_disconnected_graph()

#     dist, last = dijkstra(g, 0)

#     assert dist[0] == 0
#     assert dist[1] == 1

#     # Unreachable nodes
#     assert dist[2] == float('inf')
#     assert dist[3] == float('inf')
#     assert last[2] == -1
#     assert last[3] == -1


# 
# # Multiple Equal Paths
# 

# def test_dijkstra_equal_paths():
#     # 0 -> 1 (1)
#     # 0 -> 2 (1)
#     # 1 -> 3 (1)
#     # 2 -> 3 (1)
#     g = Graph(4)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(0, 2, 1.0)
#     g.insert_edge(1, 3, 1.0)
#     g.insert_edge(2, 3, 1.0)

#     dist, last = dijkstra(g, 0)

#     assert dist[3] == 2

#     path = make_node_path_from_last(last, 3)
#     assert len(path) == 3  # either 0-1-3 or 0-2-3


# 
# # Single Node Graph
# 

# def test_dijkstra_single_node():
#     g = Graph(1)

#     dist, last = dijkstra(g, 0)

#     assert dist == [0]
#     assert last == [-1]