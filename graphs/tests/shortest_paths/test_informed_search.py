# tests/shortest_paths/test_informed_search.py

import pytest
from graphs.core.graph import Graph
from graphs.shortest_paths.informed_search import greedy_search
from graphs.utils import make_node_path_from_last


def test_greedy_search_simple():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(0, 2, 5.0)

    h = [2.0, 1.0, 0.0]
    last = greedy_search(g, h, 0, 2)
    path = make_node_path_from_last(last, 2)
    assert 2 in path
    assert path[0] == 0


def test_greedy_search_direct_path():
    g = Graph(2, undirected=True)
    g.insert_edge(0, 1, 1.0)

    h = [1.0, 0.0]
    last = greedy_search(g, h, 0, 1)
    path = make_node_path_from_last(last, 1)
    assert path == [0, 1]


def test_greedy_search_unreachable():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    # No path to node 2
    h = [2.0, 1.0, 0.0]
    last = greedy_search(g, h, 0, 2)
    assert last[2] == -1


def test_greedy_search_already_at_goal():
    g = Graph(2, undirected=True)
    g.insert_edge(0, 1, 1.0)

    h = [0.0, 1.0]
    last = greedy_search(g, h, 0, 0)
    # Start is goal, so nothing explored
    assert last[0] == -1
