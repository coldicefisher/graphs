# tests/traversal/test_dfs.py

import pytest
from graphs.core.graph import Graph
from graphs.traversal.dfs_search import (
    depth_first_search_basic,
    depth_first_basic_all,
    depth_first_search_path,
    depth_first_search_stack,
    dfs_connected_components,
    topological_dfs,
)
from graphs.utils import check_last_path_valid



# Helper Graph Builders


def make_chain_graph():
    # 0 -> 1 -> 2 -> 3
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g


def make_disconnected_graph():
    # Component 1: 0-1
    # Component 2: 2-3
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g


def make_dag():
    # 0 → 1 → 3
    # 0 → 2 → 3
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(2, 3, 1.0)
    return g



# Basic DFS Reachability


def test_depth_first_search_basic():
    g = make_chain_graph()
    seen = depth_first_search_basic(g, 0)

    assert seen == [True, True, True, True]


def test_depth_first_basic_all():
    g = make_disconnected_graph()
    seen = depth_first_basic_all(g)

    assert seen == [True, True, True, True]



# DFS Parent Tracking


def test_depth_first_search_path():
    g = make_chain_graph()
    last = depth_first_search_path(g)

    assert check_last_path_valid(g, last)


def test_depth_first_search_stack():
    g = make_chain_graph()
    last = depth_first_search_stack(g, 0)

    assert check_last_path_valid(g, last)


def test_recursive_and_stack_consistency():
    g = make_chain_graph()

    last_recursive = depth_first_search_path(g)
    last_stack = depth_first_search_stack(g, 0)

    assert check_last_path_valid(g, last_recursive)
    assert check_last_path_valid(g, last_stack)



# Connected Components


def test_connected_components():
    g = make_disconnected_graph()

    components = dfs_connected_components(g)

    # Expect 2 components
    assert len(set(components)) == 2

    # 0 and 1 same
    assert components[0] == components[1]

    # 2 and 3 same
    assert components[2] == components[3]

    # Different components
    assert components[0] != components[2]



# Topological Sort


def test_topological_dfs_valid_order():
    g = make_dag()

    ordering = topological_dfs(g)

    # Valid topo order length
    assert len(ordering) == g.num_nodes

    # Check ordering validity
    pos = {node: i for i, node in enumerate(ordering)}

    for node in g.nodes:
        for edge in node.get_edge_list():
            assert pos[edge.from_node] < pos[edge.to_node]



# Edge Case: Single Node


def test_single_node_graph():
    g = Graph(1)

    seen = depth_first_search_basic(g, 0)
    assert seen == [True]

    components = dfs_connected_components(g)
    assert components == [0]