"""
Chapter 17: Dynamic A* Search
Demonstrates A* search using the World abstraction for dynamic state spaces.
"""

import math
from graphs.core.graph import Graph
from graphs.world import World, astar_dynamic
from graphs.utils import make_node_path_from_last


def dynamic_astar_grid():
    """A* on a grid using the World abstraction."""
    print("=== Dynamic A* on Grid ===")
    # 3x3 grid with coordinates as labels
    g = Graph(9, undirected=True)
    for r in range(3):
        for c in range(3):
            idx = r * 3 + c
            g.nodes[idx].label = (c, r)
            if c < 2:
                g.insert_edge(idx, idx + 1, 1.0)
            if r < 2:
                g.insert_edge(idx, idx + 3, 1.0)

    w = World(g, 0, 8)  # top-left to bottom-right
    last = astar_dynamic(w)

    # Reconstruct path
    path = []
    current = 8
    while current != -1:
        path.append(current)
        current = last.get(current, -1)
    path.reverse()

    print(f"Path from (0,0) to (2,2): {path}")
    print(f"Coordinates: {[g.nodes[n].label for n in path]}")
    print()


def dynamic_astar_weighted():
    """A* with varying edge costs."""
    print("=== Dynamic A* with Weighted Edges ===")
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 5.0)
    g.insert_edge(1, 3, 5.0)
    g.insert_edge(2, 3, 1.0)
    for i in range(4):
        g.nodes[i].label = (i % 2, i // 2)

    w = World(g, 0, 3)
    last = astar_dynamic(w)

    path = []
    current = 3
    while current != -1:
        path.append(current)
        current = last.get(current, -1)
    path.reverse()

    print(f"Optimal path: {path}")
    print()


def main():
    dynamic_astar_grid()
    dynamic_astar_weighted()


if __name__ == "__main__":
    main()
