# tests/metrics/test_diameter.py

import pytest
from graphs.core.graph import Graph
from graphs.metrics.diameter import graph_diameter


def test_diameter_chain():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    assert graph_diameter(g) == 2.0


def test_diameter_triangle():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(0, 2, 1.0)
    assert graph_diameter(g) == 1.0


def test_diameter_single_node():
    g = Graph(1)
    assert graph_diameter(g) == 0.0


def test_diameter_weighted():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 3.0)
    g.insert_edge(1, 2, 5.0)
    assert graph_diameter(g) == 8.0
