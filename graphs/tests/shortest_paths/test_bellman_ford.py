# tests/shortest_paths/test_bellman_ford.py

import pytest
from graphs.core.graph import Graph
from graphs.shortest_paths.bellman_ford import bellman_ford
from graphs.utils import make_node_path_from_last


def test_bellman_ford_simple():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(0, 2, 4.0)

    last = bellman_ford(g, 0)
    assert last is not None
    path = make_node_path_from_last(last, 2)
    assert path == [0, 1, 2]


def test_bellman_ford_chain():
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)

    last = bellman_ford(g, 0)
    assert last is not None
    path = make_node_path_from_last(last, 3)
    assert path == [0, 1, 2, 3]


def test_bellman_ford_negative_weights():
    g = Graph(3)
    g.insert_edge(0, 1, 4.0)
    g.insert_edge(0, 2, 5.0)
    g.insert_edge(1, 2, -2.0)

    last = bellman_ford(g, 0)
    assert last is not None
    path = make_node_path_from_last(last, 2)
    assert path == [0, 1, 2]


def test_bellman_ford_negative_cycle():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, -3.0)
    g.insert_edge(2, 0, 1.0)

    last = bellman_ford(g, 0)
    assert last is None


def test_bellman_ford_single_node():
    g = Graph(1)
    last = bellman_ford(g, 0)
    assert last is not None
    assert last == [-1]


def test_bellman_ford_disconnected():
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)

    last = bellman_ford(g, 0)
    assert last is not None
    assert last[0] == -1
    assert last[1] == 0
    assert last[2] == -1
    assert last[3] == -1
