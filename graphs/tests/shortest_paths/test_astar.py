# tests/shortest_paths/test_astar.py

import pytest
from graphs.core.graph import Graph
from graphs.world import World, astar_dynamic
from graphs.utils import make_node_path_from_last



# Helper Graph Builders


def make_simple_weighted_graph():
    # 0 --1-- 1 --2-- 2
    #  \             /
    #   \----4------- 
    g = Graph(3, undirected=True)
    g.nodes[0].label = (0, 0)
    g.nodes[1].label = (1, 0)
    g.nodes[2].label = (2, 0)

    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(0, 2, 4.0)

    return g


def make_grid_graph():
    # 2x2 grid
    # (0,0) -- (1,0)
    #   |         |
    # (0,1) -- (1,1)

    g = Graph(4, undirected=True)

    coords = [(0,0), (1,0), (0,1), (1,1)]
    for i, pos in enumerate(coords):
        g.nodes[i].label = pos

    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(2, 3, 1.0)

    return g



# Tests


def test_astar_simple_graph():
    g = make_simple_weighted_graph()
    w = World(g, start_ind=0, goal_ind=2)

    last = astar_dynamic(w)
    path = make_node_path_from_last(last, 2)

    # Optimal path is 0 → 1 → 2
    assert path == [0, 1, 2]


def test_astar_grid():
    g = make_grid_graph()
    w = World(g, start_ind=0, goal_ind=3)

    last = astar_dynamic(w)
    path = make_node_path_from_last(last, 3)

    # Path length must be 3 nodes (2 moves)
    assert len(path) == 3
    assert path[0] == 0
    assert path[-1] == 3


def test_astar_same_as_dijkstra_when_direct():
    # Straight chain
    g = Graph(4, undirected=True)
    for i in range(4):
        g.nodes[i].label = (i, 0)

    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)

    w = World(g, start_ind=0, goal_ind=3)
    last = astar_dynamic(w)
    path = make_node_path_from_last(last, 3)

    assert path == [0, 1, 2, 3]


def test_astar_unreachable():
    g = Graph(4, undirected=True)
    g.nodes[0].label = (0,0)
    g.nodes[1].label = (1,0)
    g.nodes[2].label = (2,0)
    g.nodes[3].label = (3,0)

    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)

    w = World(g, start_ind=0, goal_ind=3)
    last = astar_dynamic(w)

    # Goal unreachable
    assert 3 not in last or last[3] == -1