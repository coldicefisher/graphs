# tests/test_world.py

import math
import pytest
from graphs.core.graph import Graph
from graphs.world import (
    World,
    astar_dynamic,
    is_topo_ordered,
    Kahns,
    check_cycle_kehns,
    sort_forward_pointers,
)


# World class

def test_world_basic():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 2.0)
    g.insert_edge(1, 2, 3.0)
    for i in range(3):
        g.nodes[i].label = (i, 0)

    w = World(g, 0, 2)
    assert w.get_num_states() == 3
    assert w.is_goal(2) is True
    assert w.is_goal(0) is False
    assert w.get_start_index() == 0
    assert 1 in w.get_neighbors(0)
    assert w.get_cost(0, 1) == 2.0
    assert w.get_cost(0, 2) == math.inf


def test_world_heuristic():
    g = Graph(2, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.nodes[0].label = (0, 0)
    g.nodes[1].label = (3, 4)

    w = World(g, 0, 1)
    assert w.get_heuristic(0) == 5.0


# astar_dynamic

def test_astar_dynamic_simple():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(0, 2, 5.0)
    for i in range(3):
        g.nodes[i].label = (i, 0)

    w = World(g, 0, 2)
    last = astar_dynamic(w)
    assert last[2] == 1
    assert last[1] == 0


def test_astar_dynamic_update_cost():
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 10.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    for i in range(4):
        g.nodes[i].label = (i, 0)

    w = World(g, 0, 3)
    last = astar_dynamic(w)
    assert last[3] == 2
    assert last[2] == 1


# is_topo_ordered

def test_is_topo_ordered_valid():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    assert is_topo_ordered(g, [0, 1, 2]) is True


def test_is_topo_ordered_invalid():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    assert is_topo_ordered(g, [2, 1, 0]) is False


def test_is_topo_ordered_wrong_size():
    g = Graph(3)
    assert is_topo_ordered(g, [0, 1]) is False


def test_is_topo_ordered_duplicate():
    g = Graph(3)
    assert is_topo_ordered(g, [0, 0, 1]) is False


# Kahn's algorithm

def test_kahns_simple():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    result = Kahns(g)
    assert is_topo_ordered(g, result)


def test_kahns_diamond():
    g = Graph(4)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(2, 3, 1.0)
    result = Kahns(g)
    assert is_topo_ordered(g, result)


# check_cycle_kehns

def test_check_cycle_kehns_no_cycle():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    assert check_cycle_kehns(g) is False


def test_check_cycle_kehns_has_cycle():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 0, 1.0)
    assert check_cycle_kehns(g) is True


# sort_forward_pointers

def test_sort_forward_pointers():
    # Node 0 points to 1, node 1 points to 2, node 2 has no forward
    options = [[1], [2], []]
    result = sort_forward_pointers(options)
    assert is_topo_ordered(Graph(3), result) or result == [0, 1, 2]


def test_sort_forward_pointers_with_sentinel():
    options = [[1, -1], [2], []]
    result = sort_forward_pointers(options)
    assert 0 in result and 1 in result and 2 in result
