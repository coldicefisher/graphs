# tests/test_utils.py

import math
import pytest
from graphs.core.graph import Graph
from graphs.core.edge import Edge
from graphs.utils import (
    check_node_path_valid,
    make_node_path_from_last,
    check_last_path_valid,
    compute_path_cost_from_edges,
    make_grid_graph,
    make_grid_with_obstacles,
    euclidean_dist,
)


# check_node_path_valid

def test_check_node_path_valid_empty():
    g = Graph(3)
    assert check_node_path_valid(g, []) is True


def test_check_node_path_valid_good_path():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    assert check_node_path_valid(g, [0, 1, 2]) is True


def test_check_node_path_valid_bad_path():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    assert check_node_path_valid(g, [0, 2]) is False


# make_node_path_from_last

def test_make_node_path_from_last():
    last = [-1, 0, 1, 2]
    path = make_node_path_from_last(last, 3)
    assert path == [0, 1, 2, 3]


def test_make_node_path_from_last_start():
    last = [-1, 0, 1]
    path = make_node_path_from_last(last, 0)
    assert path == [0]


# check_last_path_valid

def test_check_last_path_valid_good():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    assert check_last_path_valid(g, [-1, 0, 1]) is True


def test_check_last_path_valid_wrong_size():
    g = Graph(3)
    assert check_last_path_valid(g, [-1, 0]) is False


def test_check_last_path_valid_bad_edge():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    assert check_last_path_valid(g, [-1, 0, 0]) is False


# compute_path_cost_from_edges

def test_compute_path_cost_empty():
    assert compute_path_cost_from_edges([]) == 0.0


def test_compute_path_cost_valid():
    edges = [Edge(0, 1, 3.0), Edge(1, 2, 4.0)]
    assert compute_path_cost_from_edges(edges) == 7.0


def test_compute_path_cost_discontinuous():
    edges = [Edge(0, 1, 3.0), Edge(5, 2, 4.0)]
    assert compute_path_cost_from_edges(edges) == math.inf


# make_grid_graph

def test_make_grid_graph():
    g = make_grid_graph(3, 2)
    assert g.num_nodes == 6
    assert g.is_edge(0, 1)
    assert g.is_edge(0, 3)
    assert not g.is_edge(2, 3)  # no wrap


# make_grid_with_obstacles

def test_make_grid_with_obstacles():
    obstacles = {(0, 1)}
    g = make_grid_with_obstacles(3, 2, obstacles)
    assert g.num_nodes == 6
    assert not g.is_edge(0, 1)  # obstacle blocks
    assert g.is_edge(0, 3)


# euclidean_dist

def test_euclidean_dist():
    assert euclidean_dist(0, 0, 3, 4) == 5.0
    assert euclidean_dist(1, 1, 1, 1) == 0.0
