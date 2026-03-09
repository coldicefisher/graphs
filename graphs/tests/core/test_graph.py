import pytest

from graphs.core.graph import Graph
from graphs.core.graph_matrix import GraphMatrix
from graphs.core.node import Node
from graphs.core.edge import Edge



# GraphMatrix Tests


def test_graph_matrix_initialization():
    g = GraphMatrix(3)
    assert g.num_nodes == 3
    assert g.undirected is False
    assert len(g.connections) == 3
    assert len(g.connections[0]) == 3


def test_graph_matrix_set_and_get_edge():
    g = GraphMatrix(3)
    g.set_edge(0, 1, 2.5)

    assert g.get_edge(0, 1) == 2.5
    assert g.get_edge(1, 0) == 0.0  # directed by default


def test_graph_matrix_undirected():
    g = GraphMatrix(3, undirected=True)
    g.set_edge(0, 1, 7.0)

    assert g.get_edge(0, 1) == 7.0
    assert g.get_edge(1, 0) == 7.0


def test_graph_matrix_invalid_index():
    g = GraphMatrix(3)

    with pytest.raises(IndexError):
        g.get_edge(-1, 0)

    with pytest.raises(IndexError):
        g.get_edge(0, 5)

    with pytest.raises(IndexError):
        g.set_edge(4, 0, 1.0)



# Node Tests


def test_node_add_and_get_edge():
    n = Node(0)
    n.add_edge(1, 4.0)

    edge = n.get_edge(1)
    assert edge is not None
    assert edge.from_node == 0
    assert edge.to_node == 1
    assert edge.weight == 4.0


def test_node_remove_edge():
    n = Node(0)
    n.add_edge(1, 2.0)
    n.remove_edge(1)

    assert n.get_edge(1) is None
    assert n.num_edges() == 0


def test_node_sorted_edge_list():
    n = Node(0)
    n.add_edge(3, 1.0)
    n.add_edge(1, 1.0)
    n.add_edge(2, 1.0)

    edges = n.get_sorted_edge_list()
    neighbors = [e.to_node for e in edges]

    assert neighbors == [1, 2, 3]



# Graph Tests


def test_graph_initialization():
    g = Graph(4)

    assert g.num_nodes == 4
    assert len(g.nodes) == 4
    assert g.undirected is False


def test_insert_and_get_edge_directed():
    g = Graph(3)
    g.insert_edge(0, 1, 5.0)

    edge = g.get_edge(0, 1)
    assert edge is not None
    assert edge.weight == 5.0

    assert g.get_edge(1, 0) is None


def test_insert_edge_undirected():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 2, 8.0)

    assert g.get_edge(0, 2) is not None
    assert g.get_edge(2, 0) is not None


def test_remove_edge_directed():
    g = Graph(3)
    g.insert_edge(0, 1, 3.0)
    g.remove_edge(0, 1)

    assert g.get_edge(0, 1) is None


def test_remove_edge_undirected():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 3.0)
    g.remove_edge(0, 1)

    assert g.get_edge(0, 1) is None
    assert g.get_edge(1, 0) is None


def test_is_edge():
    g = Graph(3)
    g.insert_edge(1, 2, 9.0)

    assert g.is_edge(1, 2) is True
    assert g.is_edge(2, 1) is False


def test_make_edge_list():
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 2.0)

    edges = g.make_edge_list()
    assert len(edges) == 2

    weights = sorted(e.weight for e in edges)
    assert weights == [1.0, 2.0]


def test_graph_invalid_index():
    g = Graph(3)

    with pytest.raises(IndexError):
        g.get_edge(-1, 1)

    with pytest.raises(IndexError):
        g.insert_edge(5, 1, 1.0)

    with pytest.raises(IndexError):
        g.remove_edge(0, 10)



# Deep Copy Tests


def test_make_copy_structure():
    g = Graph(3, undirected=True)
    g.nodes[0].label = "A"
    g.insert_edge(0, 1, 4.0)

    g2 = g.make_copy()

    # Verify node labels copied
    assert g2.nodes[0].label == "A"

    # Verify edges copied
    assert g2.get_edge(0, 1) is not None
    assert g2.get_edge(1, 0) is not None

    # Ensure it's a different object
    assert g2 is not g


def test_make_copy_independent():
    g = Graph(3)
    g.insert_edge(0, 1, 5.0)

    g2 = g.make_copy()

    # Modify original
    g.remove_edge(0, 1)

    # Copy should remain unchanged
    assert g.get_edge(0, 1) is None
    assert g2.get_edge(0, 1) is not None


# get_in_neighbors

def test_get_in_neighbors():
    g = Graph(3)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 2, 1.0)
    neighbors = g.get_in_neighbors(2)
    assert neighbors == {0, 1}


# clustering_coefficient

def test_clustering_coefficient_triangle():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(0, 2, 1.0)
    assert g.clustering_coefficient(0) == 1.0


def test_clustering_coefficient_no_edges_between_neighbors():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    assert g.clustering_coefficient(0) == 0.0


def test_clustering_coefficient_single_neighbor():
    g = Graph(2, undirected=True)
    g.insert_edge(0, 1, 1.0)
    assert g.clustering_coefficient(0) == 0.0


def test_clustering_coefficient_directed_raises():
    g = Graph(3)
    with pytest.raises(ValueError):
        g.clustering_coefficient(0)


# average_clustering_coefficient

def test_average_clustering_coefficient():
    g = Graph(3, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(0, 2, 1.0)
    avg = g.average_clustering_coefficient()
    assert avg == 1.0


def test_average_clustering_coefficient_empty():
    g = Graph(0, undirected=True)
    assert g.average_clustering_coefficient() == 0.0


# make_undirected_neighborhood_subgraph

def test_neighborhood_subgraph_closed():
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)

    sub = g.make_undirected_neighborhood_subgraph(0, closed=True)
    assert sub.num_nodes == 3  # nodes 0, 1, 2


def test_neighborhood_subgraph_open():
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 2, 1.0)

    sub = g.make_undirected_neighborhood_subgraph(0, closed=False)
    assert sub.num_nodes == 2  # nodes 1, 2 only


def test_neighborhood_subgraph_directed_raises():
    g = Graph(3)
    with pytest.raises(ValueError):
        g.make_undirected_neighborhood_subgraph(0, closed=True)


# insert_node

def test_insert_node():
    g = Graph(2)
    new_node = g.insert_node(label="new")
    assert g.num_nodes == 3
    assert new_node.index == 2
    assert new_node.label == "new"


# Node.get_out_neighbors

def test_node_get_out_neighbors():
    n = Node(0)
    n.add_edge(1, 1.0)
    n.add_edge(2, 1.0)
    assert n.get_out_neighbors() == {1, 2}


# Node.remove_edge nonexistent

def test_node_remove_nonexistent_edge():
    n = Node(0)
    n.remove_edge(99)  # should not raise
    assert n.num_edges() == 0


# Graph.remove_edge to_node bounds check

def test_remove_edge_invalid_to_node():
    g = Graph(3)
    with pytest.raises(IndexError):
        g.remove_edge(-1, 0)