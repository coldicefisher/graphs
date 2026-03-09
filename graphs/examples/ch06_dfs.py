"""
Chapter 6: Depth-First Search
Demonstrates DFS traversal, connected components, and topological sort.
"""

from graphs.core.graph import Graph
from graphs.traversal.dfs_search import (
    depth_first_search_basic,
    depth_first_basic_all,
    depth_first_search_path,
    depth_first_search_stack,
    dfs_connected_components,
    topological_dfs,
)


def dfs_basic_example():
    """Run basic DFS and show which nodes are reachable."""
    print("=== Basic DFS ===")
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(3, 4, 1.0)

    seen = depth_first_search_basic(g, 0)
    print(f"Reachable from node 0: {[i for i, s in enumerate(seen) if s]}")

    seen_all = depth_first_basic_all(g)
    print(f"All nodes visited: {all(seen_all)}")
    print()


def dfs_path_example():
    """DFS with path tracking - recursive and stack-based."""
    print("=== DFS Path Tracking ===")
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(3, 4, 1.0)

    last_recursive = depth_first_search_path(g)
    print(f"Recursive parent array: {last_recursive}")

    last_stack = depth_first_search_stack(g, 0)
    print(f"Stack-based parent array: {last_stack}")
    print()


def connected_components_example():
    """Find connected components using DFS."""
    print("=== Connected Components ===")
    g = Graph(7, undirected=True)
    # Component 0: nodes 0, 1, 2
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    # Component 1: nodes 3, 4
    g.insert_edge(3, 4, 1.0)
    # Component 2: nodes 5, 6
    g.insert_edge(5, 6, 1.0)

    components = dfs_connected_components(g)
    print(f"Component labels: {components}")

    num_components = max(components) + 1
    for c in range(num_components):
        nodes = [i for i, comp in enumerate(components) if comp == c]
        print(f"  Component {c}: {nodes}")
    print()


def topological_sort_example():
    """Topological sort on a DAG (course prerequisites)."""
    print("=== Topological Sort ===")
    # Course dependencies:
    # 0: Intro -> 1: Data Structures
    # 0: Intro -> 2: Algorithms
    # 1: Data Structures -> 3: Databases
    # 2: Algorithms -> 3: Databases
    # 2: Algorithms -> 4: AI
    g = Graph(5)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(2, 4, 1.0)

    ordering = topological_dfs(g)
    print(f"Topological order: {ordering}")

    courses = ["Intro", "Data Structures", "Algorithms", "Databases", "AI"]
    print("Course order:")
    for i, node in enumerate(ordering):
        print(f"  {i + 1}. {courses[node]}")
    print()


def main():
    dfs_basic_example()
    dfs_path_example()
    connected_components_example()
    topological_sort_example()


if __name__ == "__main__":
    main()
