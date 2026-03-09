"""
Chapter 8: All-Pairs Shortest Paths
Demonstrates Floyd-Warshall algorithm and graph diameter computation.
"""

import math
from graphs.core.graph import Graph
from graphs.shortest_paths.floyd_warshall import floyd_warshall
from graphs.metrics.diameter import graph_diameter


def floyd_warshall_example():
    """Compute all-pairs shortest paths."""
    print("=== Floyd-Warshall Algorithm ===")
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 3.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 2.0)
    g.insert_edge(0, 3, 10.0)

    dist = floyd_warshall(g)

    print("Distance matrix:")
    for i in range(g.num_nodes):
        row = []
        for j in range(g.num_nodes):
            if dist[i][j] == math.inf:
                row.append(" inf")
            else:
                row.append(f"{dist[i][j]:4.0f}")
        print(f"  {i}: [{', '.join(row)}]")
    print()


def diameter_example():
    """Compute graph diameter (longest shortest path)."""
    print("=== Graph Diameter ===")

    # Chain graph: 0 - 1 - 2 - 3
    g1 = Graph(4, undirected=True)
    g1.insert_edge(0, 1, 1.0)
    g1.insert_edge(1, 2, 1.0)
    g1.insert_edge(2, 3, 1.0)
    print(f"Chain 0-1-2-3 diameter: {graph_diameter(g1)}")

    # Complete graph (triangle)
    g2 = Graph(3, undirected=True)
    g2.insert_edge(0, 1, 1.0)
    g2.insert_edge(1, 2, 1.0)
    g2.insert_edge(0, 2, 1.0)
    print(f"Triangle diameter: {graph_diameter(g2)}")
    print()


def main():
    floyd_warshall_example()
    diameter_example()


if __name__ == "__main__":
    main()
