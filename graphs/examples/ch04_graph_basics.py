"""
Chapter 4: Storing Graphs
Demonstrates adjacency list and adjacency matrix representations.
"""

from graphs.core.graph import Graph
from graphs.core.graph_matrix import GraphMatrix
from graphs.core.edge import Edge
from graphs.core.node import Node


def adjacency_list_example():
    """Build a small social network using an adjacency list graph."""
    print("=== Adjacency List Graph ===")
    g = Graph(5, undirected=True)

    # Add friendships
    g.insert_edge(0, 1, 1.0)  # Alice - Bob
    g.insert_edge(0, 2, 1.0)  # Alice - Carol
    g.insert_edge(1, 3, 1.0)  # Bob - Dave
    g.insert_edge(2, 3, 1.0)  # Carol - Dave
    g.insert_edge(3, 4, 1.0)  # Dave - Eve

    print(f"Number of nodes: {g.num_nodes}")
    print(f"Is undirected: {g.undirected}")
    print(f"Edge 0->1 exists: {g.is_edge(0, 1)}")
    print(f"Edge 0->4 exists: {g.is_edge(0, 4)}")

    edges = g.make_edge_list()
    print(f"Total directed edges (2x undirected): {len(edges)}")

    # In-neighbors of node 3
    in_neighbors = g.get_in_neighbors(3)
    print(f"In-neighbors of node 3: {in_neighbors}")

    # Make a copy
    g2 = g.make_copy()
    g2.remove_edge(0, 1)
    print(f"Original still has 0->1: {g.is_edge(0, 1)}")
    print(f"Copy has 0->1: {g2.is_edge(0, 1)}")
    print()


def adjacency_matrix_example():
    """Build a weighted graph using an adjacency matrix."""
    print("=== Adjacency Matrix Graph ===")
    gm = GraphMatrix(4, undirected=True)

    gm.set_edge(0, 1, 5.0)
    gm.set_edge(1, 2, 3.0)
    gm.set_edge(2, 3, 7.0)
    gm.set_edge(0, 3, 10.0)

    print(f"Weight 0->1: {gm.get_edge(0, 1)}")
    print(f"Weight 1->0 (symmetric): {gm.get_edge(1, 0)}")
    print(f"Weight 0->2 (no edge): {gm.get_edge(0, 2)}")
    print()


def node_operations_example():
    """Demonstrate node-level operations."""
    print("=== Node Operations ===")
    n = Node(0, label="Alice")
    n.add_edge(1, 2.0)
    n.add_edge(2, 5.0)
    n.add_edge(3, 1.0)

    print(f"Node {n.index} ({n.label})")
    print(f"Number of edges: {n.num_edges()}")
    print(f"Neighbors: {n.get_neighbors()}")

    sorted_edges = n.get_sorted_edge_list()
    print(f"Sorted neighbors: {[e.to_node for e in sorted_edges]}")

    n.remove_edge(2)
    print(f"After removing edge to 2, neighbors: {n.get_neighbors()}")
    print()


def dynamic_graph_example():
    """Demonstrate adding nodes dynamically."""
    print("=== Dynamic Node Insertion ===")
    g = Graph(2, undirected=True)
    g.insert_edge(0, 1, 1.0)
    print(f"Initial nodes: {g.num_nodes}")

    new_node = g.insert_node(label="new")
    g.insert_edge(1, new_node.index, 3.0)
    print(f"After insert_node: {g.num_nodes}")
    print(f"New node index: {new_node.index}, label: {new_node.label}")
    print(f"Edge 1->{new_node.index}: {g.is_edge(1, new_node.index)}")
    print()


def main():
    adjacency_list_example()
    adjacency_matrix_example()
    node_operations_example()
    dynamic_graph_example()


if __name__ == "__main__":
    main()
