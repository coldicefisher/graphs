"""
Chapter 7: Shortest Paths
Demonstrates Dijkstra's algorithm and Bellman-Ford on weighted graphs.
"""

import math
from graphs.core.graph import Graph
from graphs.shortest_paths.dijkstra import dijkstra
from graphs.shortest_paths.bellman_ford import bellman_ford
from graphs.utils import make_node_path_from_last


def dijkstra_example():
    """Find shortest paths in a weighted graph using Dijkstra's algorithm."""
    print("=== Dijkstra's Algorithm ===")
    #       1
    #   0 ----- 1
    #   |       /|
    #  4|    2/  |3
    #   |   /    |
    #   2 ----- 3
    #       5
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 4.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(1, 3, 3.0)
    g.insert_edge(2, 3, 5.0)

    dist, last = dijkstra(g, 0)

    print("From node 0:")
    for i in range(g.num_nodes):
        path = make_node_path_from_last(last, i)
        print(f"  To {i}: distance={dist[i]}, path={path}")
    print()


def bellman_ford_example():
    """Bellman-Ford handles negative edge weights."""
    print("=== Bellman-Ford Algorithm ===")
    g = Graph(4)
    g.insert_edge(0, 1, 4.0)
    g.insert_edge(0, 2, 5.0)
    g.insert_edge(1, 2, -2.0)
    g.insert_edge(2, 3, 3.0)

    last = bellman_ford(g, 0)
    if last is not None:
        for i in range(g.num_nodes):
            path = make_node_path_from_last(last, i)
            print(f"  To {i}: path={path}")
    else:
        print("  Negative cycle detected!")
    print()


def bellman_ford_negative_cycle():
    """Demonstrate negative cycle detection."""
    print("=== Negative Cycle Detection ===")
    g = Graph(3)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, -3.0)
    g.insert_edge(2, 0, 1.0)

    last = bellman_ford(g, 0)
    if last is None:
        print("  Negative cycle detected - no shortest paths exist!")
    print()


def main():
    dijkstra_example()
    bellman_ford_example()
    bellman_ford_negative_cycle()


if __name__ == "__main__":
    main()
