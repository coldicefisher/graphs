"""
Chapter 10: Minimum Spanning Trees
Demonstrates Prim's and Kruskal's algorithms.
"""

from graphs.core.graph import Graph
from graphs.mst.prims import prims
from graphs.mst.kruskals import kruskals, randomized_kruskals


def prims_example():
    """Find MST using Prim's algorithm."""
    print("=== Prim's Algorithm ===")
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 2.0)
    g.insert_edge(0, 3, 6.0)
    g.insert_edge(1, 2, 3.0)
    g.insert_edge(1, 3, 8.0)
    g.insert_edge(1, 4, 5.0)
    g.insert_edge(2, 4, 7.0)
    g.insert_edge(3, 4, 9.0)

    mst = prims(g)
    if mst is not None:
        total = sum(e.weight for e in mst)
        print(f"MST edges ({len(mst)} edges, total weight {total}):")
        for e in mst:
            print(f"  {e.from_node} -- {e.to_node} (weight {e.weight})")
    else:
        print("Graph is disconnected - no MST exists")
    print()


def kruskals_example():
    """Find MST using Kruskal's algorithm."""
    print("=== Kruskal's Algorithm ===")
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 2.0)
    g.insert_edge(0, 3, 6.0)
    g.insert_edge(1, 2, 3.0)
    g.insert_edge(1, 3, 8.0)
    g.insert_edge(1, 4, 5.0)
    g.insert_edge(2, 4, 7.0)
    g.insert_edge(3, 4, 9.0)

    mst = kruskals(g)
    if mst is not None:
        total = sum(e.weight for e in mst)
        print(f"MST edges ({len(mst)} edges, total weight {total}):")
        for e in mst:
            print(f"  {e.from_node} -- {e.to_node} (weight {e.weight})")
    else:
        print("Graph is disconnected - no MST exists")
    print()


def randomized_kruskals_example():
    """Generate a random spanning tree (maze generation)."""
    print("=== Randomized Kruskal's (Maze Generation) ===")
    # Create a 3x3 grid
    g = Graph(9, undirected=True)
    for r in range(3):
        for c in range(3):
            idx = r * 3 + c
            if c < 2:
                g.insert_edge(idx, idx + 1, 1.0)
            if r < 2:
                g.insert_edge(idx, idx + 3, 1.0)

    maze = randomized_kruskals(g)
    print(f"Maze edges ({len(maze)} passages):")
    for e in maze:
        print(f"  {e.from_node} -- {e.to_node}")
    print()


def disconnected_mst_example():
    """Show that MST algorithms return None for disconnected graphs."""
    print("=== Disconnected Graph (No MST) ===")
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(2, 3, 1.0)

    mst_p = prims(g)
    mst_k = kruskals(g)
    print(f"Prim's result: {mst_p}")
    print(f"Kruskal's result: {mst_k}")
    print()


def main():
    prims_example()
    kruskals_example()
    randomized_kruskals_example()
    disconnected_mst_example()


if __name__ == "__main__":
    main()
