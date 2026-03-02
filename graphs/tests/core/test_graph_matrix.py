# tests/core/test_graph_matrix.py

import pytest
from graphs.core.graph_matrix import GraphMatrix



# Initialization Tests


def test_graph_matrix_initialization_directed():
    g = GraphMatrix(4)

    assert g.num_nodes == 4
    assert g.undirected is False
    assert len(g.connections) == 4
    assert all(len(row) == 4 for row in g.connections)

    # All weights should default to 0.0
    for r in range(4):
        for c in range(4):
            assert g.connections[r][c] == 0.0


def test_graph_matrix_initialization_undirected():
    g = GraphMatrix(3, undirected=True)

    assert g.num_nodes == 3
    assert g.undirected is True



# Edge Setting / Getting


def test_set_and_get_edge_directed():
    g = GraphMatrix(3)

    g.set_edge(0, 1, 2.5)

    assert g.get_edge(0, 1) == 2.5
    assert g.get_edge(1, 0) == 0.0  # Directed graph


def test_set_and_get_edge_undirected():
    g = GraphMatrix(3, undirected=True)

    g.set_edge(0, 2, 7.0)

    assert g.get_edge(0, 2) == 7.0
    assert g.get_edge(2, 0) == 7.0


def test_overwrite_edge_weight():
    g = GraphMatrix(3)

    g.set_edge(0, 1, 5.0)
    g.set_edge(0, 1, 9.0)

    assert g.get_edge(0, 1) == 9.0



# Bounds Checking


def test_get_edge_invalid_indices():
    g = GraphMatrix(3)

    with pytest.raises(IndexError):
        g.get_edge(-1, 0)

    with pytest.raises(IndexError):
        g.get_edge(0, -1)

    with pytest.raises(IndexError):
        g.get_edge(3, 0)

    with pytest.raises(IndexError):
        g.get_edge(0, 3)


def test_set_edge_invalid_indices():
    g = GraphMatrix(3)

    with pytest.raises(IndexError):
        g.set_edge(-1, 0, 1.0)

    with pytest.raises(IndexError):
        g.set_edge(0, -1, 1.0)

    with pytest.raises(IndexError):
        g.set_edge(3, 0, 1.0)

    with pytest.raises(IndexError):
        g.set_edge(0, 3, 1.0)



# Structural Integrity Tests


def test_matrix_structure_integrity():
    g = GraphMatrix(5)

    # Ensure matrix remains square after operations
    g.set_edge(0, 4, 3.0)

    assert len(g.connections) == 5
    assert all(len(row) == 5 for row in g.connections)


def test_no_unintended_symmetry_in_directed_graph():
    g = GraphMatrix(4)

    g.set_edge(1, 3, 6.0)

    assert g.get_edge(1, 3) == 6.0
    assert g.get_edge(3, 1) == 0.0