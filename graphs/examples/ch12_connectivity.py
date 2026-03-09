"""
Chapter 12: Connectivity - Bridges and Articulation Points
Demonstrates finding critical edges and nodes in a graph.
"""

from graphs.core.graph import Graph
from graphs.connectivity.structural import find_bridges, find_articulation_points


def bridges_example():
    """Find bridges (edges whose removal disconnects the graph)."""
    print("=== Finding Bridges ===")
    # Graph with a bridge between the two triangles:
    # 0--1--2--3--4
    # |  |     |  |
    # 5--6     7--8
    g = Graph(9, undirected=True)
    # Left triangle-ish component
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 5, 1.0)
    g.insert_edge(1, 6, 1.0)
    g.insert_edge(5, 6, 1.0)
    # Bridge
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    # Right triangle-ish component
    g.insert_edge(3, 4, 1.0)
    g.insert_edge(3, 7, 1.0)
    g.insert_edge(4, 8, 1.0)
    g.insert_edge(7, 8, 1.0)

    bridges = find_bridges(g)
    print(f"Number of bridges: {len(bridges)}")
    for b in bridges:
        print(f"  Bridge: {b.from_node} -- {b.to_node}")
    print()


def articulation_points_example():
    """Find articulation points (nodes whose removal disconnects the graph)."""
    print("=== Finding Articulation Points ===")
    # Star graph: node 0 connects to all others
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 1.0)

    ap = find_articulation_points(g)
    print(f"Articulation points: {ap}")
    print()


def chain_bridges_example():
    """Every edge in a chain is a bridge."""
    print("=== Chain Graph (All Bridges) ===")
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)

    bridges = find_bridges(g)
    ap = find_articulation_points(g)

    print(f"Bridges: {[(b.from_node, b.to_node) for b in bridges]}")
    print(f"Articulation points: {ap}")
    print()


def cycle_no_bridges_example():
    """A cycle has no bridges or articulation points."""
    print("=== Cycle Graph (No Bridges) ===")
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(3, 0, 1.0)

    bridges = find_bridges(g)
    ap = find_articulation_points(g)

    print(f"Bridges: {len(bridges)}")
    print(f"Articulation points: {len(ap)}")
    print()


def main():
    bridges_example()
    articulation_points_example()
    chain_bridges_example()
    cycle_no_bridges_example()


if __name__ == "__main__":
    main()
