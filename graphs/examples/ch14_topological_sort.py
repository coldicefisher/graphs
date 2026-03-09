"""
Chapter 14: Topological Sort
Demonstrates DFS-based and Kahn's algorithm for topological ordering.
"""

from graphs.core.graph import Graph
from graphs.traversal.dfs_search import topological_dfs
from graphs.world import is_topo_ordered, Kahns, check_cycle_kehns, sort_forward_pointers


def dfs_topo_sort_example():
    """Topological sort using DFS."""
    print("=== DFS Topological Sort ===")
    # Task dependencies
    tasks = ["Wake up", "Shower", "Get dressed", "Eat breakfast",
             "Brush teeth", "Leave house"]
    g = Graph(6)
    g.insert_edge(0, 1, 1.0)  # wake up -> shower
    g.insert_edge(0, 3, 1.0)  # wake up -> eat breakfast
    g.insert_edge(1, 2, 1.0)  # shower -> get dressed
    g.insert_edge(3, 4, 1.0)  # eat breakfast -> brush teeth
    g.insert_edge(2, 5, 1.0)  # get dressed -> leave
    g.insert_edge(4, 5, 1.0)  # brush teeth -> leave

    ordering = topological_dfs(g)
    print("Task order:")
    for i, node in enumerate(ordering):
        print(f"  {i + 1}. {tasks[node]}")

    valid = is_topo_ordered(g, ordering)
    print(f"Valid topological order: {valid}")
    print()


def kahns_example():
    """Topological sort using Kahn's algorithm (BFS-based)."""
    print("=== Kahn's Algorithm ===")
    g = Graph(5)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(2, 4, 1.0)

    result = Kahns(g)
    print(f"Topological order: {result}")
    print(f"Valid: {is_topo_ordered(g, result)}")
    print()


def cycle_detection_example():
    """Detect cycles using Kahn's algorithm."""
    print("=== Cycle Detection ===")

    # DAG (no cycle)
    g1 = Graph(3)
    g1.insert_edge(0, 1, 1.0)
    g1.insert_edge(1, 2, 1.0)
    print(f"DAG has cycle: {check_cycle_kehns(g1)}")

    # Graph with cycle
    g2 = Graph(3)
    g2.insert_edge(0, 1, 1.0)
    g2.insert_edge(1, 2, 1.0)
    g2.insert_edge(2, 0, 1.0)
    print(f"Cyclic graph has cycle: {check_cycle_kehns(g2)}")
    print()


def forward_pointers_example():
    """Sort forward pointers into topological order."""
    print("=== Sort Forward Pointers ===")
    # Each element lists which elements must come after it
    options = [[1, 2], [3], [3], []]
    result = sort_forward_pointers(options)
    print(f"Input forward pointers: {options}")
    print(f"Sorted order: {result}")
    print()


def main():
    dfs_topo_sort_example()
    kahns_example()
    cycle_detection_example()
    forward_pointers_example()


if __name__ == "__main__":
    main()
