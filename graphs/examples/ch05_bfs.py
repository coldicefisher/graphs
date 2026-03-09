"""
Chapter 5: Breadth-First Search
Demonstrates BFS traversal and shortest path finding in unweighted graphs.
"""

from graphs.core.graph import Graph
from graphs.traversal.bfs_search import breadth_first_search, make_grid_graph
from graphs.utils import make_node_path_from_last


def bfs_basic_example():
    """Run BFS on a simple graph and trace the search tree."""
    print("=== BFS on Simple Graph ===")
    #     0
    #    / \
    #   1   2
    #  / \   \
    # 3   4   5
    g = Graph(6, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(1, 4, 1.0)
    g.insert_edge(2, 5, 1.0)

    last = breadth_first_search(g, 0)
    print(f"Parent array: {last}")

    for dest in range(g.num_nodes):
        path = make_node_path_from_last(last, dest)
        print(f"Path to {dest}: {path}")
    print()


def bfs_grid_example():
    """Run BFS on a grid graph to find shortest paths."""
    print("=== BFS on 4x3 Grid ===")
    g = make_grid_graph(4, 3)
    # Grid layout:
    # 0  1  2  3
    # 4  5  6  7
    # 8  9  10 11

    last = breadth_first_search(g, 0)

    # Shortest path from top-left to bottom-right
    path = make_node_path_from_last(last, 11)
    print(f"Shortest path 0 -> 11: {path}")
    print(f"Path length: {len(path) - 1} edges")
    print()


def bfs_disconnected_example():
    """Show BFS behavior on a disconnected graph."""
    print("=== BFS on Disconnected Graph ===")
    g = Graph(6, undirected=True)
    # Component 1: 0-1-2
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    # Component 2: 3-4-5
    g.insert_edge(3, 4, 1.0)
    g.insert_edge(4, 5, 1.0)

    last = breadth_first_search(g, 0)
    print(f"Parent array from node 0: {last}")
    print(f"Node 2 reachable: {last[2] != -1 or 2 == 0}")
    print(f"Node 4 reachable: {last[4] != -1}")
    print()


def main():
    bfs_basic_example()
    bfs_grid_example()
    bfs_disconnected_example()


if __name__ == "__main__":
    main()
