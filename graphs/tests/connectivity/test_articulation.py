# tests/connectivity/test_articulation.py

import pytest
from graphs.core.graph import Graph
from graphs.connectivity.structural import find_articulation_points



# Helper Graph Builders


def make_chain_graph():
    # 0 - 1 - 2 - 3
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g


def make_cycle_graph():
    # 0 - 1 - 2 - 3 - 0
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(3, 0, 1.0)
    return g


def make_star_graph():
    #     1
    #     |
    # 2 - 0 - 3
    #     |
    #     4
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 1.0)
    return g


def make_disconnected_graph():
    # Component 1: 0 - 1 - 2
    # Component 2: 3 - 4
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(3, 4, 1.0)
    return g



# Tests


def test_chain_graph():
    g = make_chain_graph()
    aps = find_articulation_points(g)

    # Middle nodes are articulation points
    assert aps == {1, 2}


def test_cycle_graph():
    g = make_cycle_graph()
    aps = find_articulation_points(g)

    # No articulation points in a cycle
    assert aps == set()


def test_star_graph():
    g = make_star_graph()
    aps = find_articulation_points(g)

    # Center node is articulation point
    assert aps == {0}


def test_disconnected_graph():
    g = make_disconnected_graph()
    aps = find_articulation_points(g)

    # Only node 1 in first component is articulation
    assert aps == {1}


def test_single_node():
    g = Graph(1, undirected=True)
    aps = find_articulation_points(g)

    assert aps == set()