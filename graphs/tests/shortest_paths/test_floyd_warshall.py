# tests/shortest_paths/test_floyd_warshall.py

import pytest
from graphs.core.graph import Graph
from graphs.shortest_paths.floyd_warshall import floyd_warshall



# Helper Graph Builders


def make_simple_graph():
    # 0 --1-- 1 --2-- 2
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 2.0)
    return g


def make_triangle_graph():
    # 0 --1-- 1
    #  \      |
    #   \4     2
    #    \    |
    #       2
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(0, 2, 4.0)
    return g


def make_disconnected_graph():
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g


def make_directed_graph():
    # 0 → 1 (3)
    # 1 → 2 (4)
    # 0 → 2 (10)
    g = Graph(3)
    g.insert_edge(0, 1, 3.0)
    g.insert_edge(1, 2, 4.0)
    g.insert_edge(0, 2, 10.0)
    return g



# Basic Shortest Paths


def test_simple_graph():
    g = make_simple_graph()
    dist = floyd_warshall(g)

    assert dist[0][0] == 0
    assert dist[0][1] == 1
    assert dist[0][2] == 3  # 0→1→2
    assert dist[2][0] == 3  # undirected symmetry


def test_triangle_relaxation():
    g = make_triangle_graph()
    dist = floyd_warshall(g)

    # Direct edge is 4, but shortest path is 1 + 2 = 3
    assert dist[0][2] == 3
    assert dist[2][0] == 3


def test_directed_graph():
    g = make_directed_graph()
    dist = floyd_warshall(g)
    assert dist[0][2] == 7  # 3 + 4
    assert dist[1][0] == float('inf')  # no reverse path



# Disconnected Handling


def test_disconnected_graph():
    g = make_disconnected_graph()
    dist = floyd_warshall(g)

    assert dist[0][1] == 1
    assert dist[0][2] == float('inf')
    assert dist[3][0] == float('inf')



# Single Node


def test_single_node():
    g = Graph(1)
    dist = floyd_warshall(g)

    assert dist == [[0]]