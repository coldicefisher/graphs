# tests/connectivity/test_bridges.py

import pytest
from graphs.core.graph import Graph
from graphs.connectivity.structural import find_bridges



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


def make_mixed_graph():
    # 0 - 1 - 2 - 3
    #     |   |
    #     4---5
    #
    # Edge 0-1 is a bridge
    # Others form a cycle
    g = Graph(6, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(3, 5, 1.0)
    g.insert_edge(5, 4, 1.0)
    g.insert_edge(4, 1, 1.0)
    return g


def make_disconnected_graph():
    # Component 1: 0 - 1
    # Component 2: 2 - 3
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g



# Tests


def edge_set(edges):
    """Convert list of Edge objects to undirected edge tuples"""
    return {tuple(sorted((e.from_node, e.to_node))) for e in edges}


def test_chain_graph():
    g = make_chain_graph()
    bridges = find_bridges(g)

    assert edge_set(bridges) == {
        (0, 1),
        (1, 2),
        (2, 3),
    }


def test_cycle_graph():
    g = make_cycle_graph()
    bridges = find_bridges(g)

    assert bridges == []


def test_star_graph():
    g = make_star_graph()
    bridges = find_bridges(g)

    assert edge_set(bridges) == {
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
    }


def test_mixed_graph():
    g = make_mixed_graph()
    bridges = find_bridges(g)

    # Only 0-1 should be a bridge
    assert edge_set(bridges) == {(0, 1)}


def test_disconnected_graph():
    g = make_disconnected_graph()
    bridges = find_bridges(g)

    assert edge_set(bridges) == {
        (0, 1),
        (2, 3),
    }


def test_single_node():
    g = Graph(1, undirected=True)
    bridges = find_bridges(g)

    assert bridges == []