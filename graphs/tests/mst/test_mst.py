# # tests/mst/test_mst.py

# import pytest
# from graphs.core.graph import Graph
# from graphs.mst.kruskals import kruskals
# from graphs.mst.prims import prims


# 
# # Helper Graph Builders
# 

# def make_simple_graph():
#     #   0
#     #  / \
#     # 1---2
#     #
#     # edges:
#     # 0-1 (1)
#     # 1-2 (2)
#     # 0-2 (3)
#     g = Graph(3, undirected=True)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(1, 2, 2.0)
#     g.insert_edge(0, 2, 3.0)
#     return g


# def make_square_graph():
#     # 0--1
#     # |  |
#     # 3--2
#     g = Graph(4, undirected=True)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(1, 2, 1.0)
#     g.insert_edge(2, 3, 1.0)
#     g.insert_edge(3, 0, 1.0)
#     return g


# def make_disconnected_graph():
#     g = Graph(4, undirected=True)
#     g.insert_edge(0, 1, 1.0)
#     g.insert_edge(2, 3, 1.0)
#     return g


# 
# # Kruskal Tests
# 

# def test_kruskals_simple_graph():
#     g = make_simple_graph()

#     mst = kruskals(g)

#     assert mst is not None
#     assert len(mst) == g.num_nodes - 1

#     total_weight = sum(edge.weight for edge in mst)
#     assert total_weight == 3.0  # 1 + 2


# def test_kruskals_square_graph():
#     g = make_square_graph()

#     mst = kruskals(g)

#     assert mst is not None
#     assert len(mst) == g.num_nodes - 1

#     total_weight = sum(edge.weight for edge in mst)
#     assert total_weight == 3.0


# def test_kruskals_disconnected_returns_none():
#     g = make_disconnected_graph()

#     mst = kruskals(g)

#     assert mst is None


# 
# # Prim's Tests
# 

# def test_prims_simple_graph():
#     g = make_simple_graph()

#     mst = prims(g)

#     assert mst is not None
#     assert len(mst) == g.num_nodes - 1

#     total_weight = sum(edge.weight for edge in mst)
#     assert total_weight == 3.0


# def test_prims_square_graph():
#     g = make_square_graph()

#     mst = prims(g)

#     assert mst is not None
#     assert len(mst) == g.num_nodes - 1

#     total_weight = sum(edge.weight for edge in mst)
#     assert total_weight == 3.0


# def test_prims_disconnected_returns_none():
#     g = make_disconnected_graph()

#     mst = prims(g)

#     assert mst is None


# 
# # Consistency Check
# 

# def test_prims_and_kruskals_same_weight():
#     g = make_simple_graph()

#     mst_k = kruskals(g)
#     mst_p = prims(g)

#     assert mst_k is not None
#     assert mst_p is not None

#     weight_k = sum(e.weight for e in mst_k)
#     weight_p = sum(e.weight for e in mst_p)

#     assert weight_k == weight_p