# tests/traversal/test_bfs.py

import pytest
from graphs.core.graph import Graph
from graphs.traversal.bfs_search import breadth_first_search
from graphs.utils import check_last_path_valid, make_node_path_from_last



# Helper Graph Builders


def make_chain_graph():
    # 0 → 1 → 2 → 3
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g


def make_branch_graph():
    #      0
    #     / \
    #    1   2
    #     \ /
    #      3
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g


def make_disconnected_graph():
    # Component 1: 0-1
    # Component 2: 2-3
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g



# Basic BFS Reachability


def test_bfs_chain_graph():
    g = make_chain_graph()

    last = breadth_first_search(g, 0)

    assert check_last_path_valid(g, last)

    path = make_node_path_from_last(last, 3)
    assert path == [0, 1, 2, 3]


def test_bfs_branch_graph_shortest_path():
    g = make_branch_graph()

    last = breadth_first_search(g, 0)

    assert check_last_path_valid(g, last)

    # Shortest path from 0 to 3 must be length 2
    path = make_node_path_from_last(last, 3)
    assert len(path) == 3  # 0 → 1 → 3 OR 0 → 2 → 3



# BFS Level Order Property


def test_bfs_levels():
    g = make_branch_graph()

    last = breadth_first_search(g, 0)

    # Node 1 and 2 should both have parent 0
    assert last[1] == 0
    assert last[2] == 0

    # Node 3 should have parent either 1 or 2
    assert last[3] in (1, 2)



# Disconnected Graph


def test_bfs_disconnected():
    g = make_disconnected_graph()

    last = breadth_first_search(g, 0)

    # Only component 1 reachable
    assert last[0] == -1
    assert last[1] == 0

    # Other component unreachable
    assert last[2] == -1
    assert last[3] == -1



# Single Node


def test_bfs_single_node():
    g = Graph(1)

    last = breadth_first_search(g, 0)

    assert last == [-1]