"""
Chapter 9: Informed Search
Demonstrates A* search and greedy best-first search with heuristics.
"""

import math
from graphs.core.graph import Graph
from graphs.shortest_paths.astar import astar_search
from graphs.shortest_paths.informed_search import greedy_search
from graphs.utils import make_node_path_from_last, euclidean_dist


def astar_example():
    """A* search on a grid-like weighted graph with coordinates."""
    print("=== A* Search ===")
    # 4-node graph with coordinates for heuristic
    # 0(0,0) -- 1(1,0)
    #   |         |
    # 2(0,1) -- 3(1,1)
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 1.0)
    g.insert_edge(1, 3, 1.0)
    g.insert_edge(2, 3, 1.0)

    coords = [(0, 0), (1, 0), (0, 1), (1, 1)]
    goal = 3
    h = [euclidean_dist(x, y, coords[goal][0], coords[goal][1])
         for x, y in coords]

    print(f"Heuristic values: {[f'{v:.2f}' for v in h]}")

    last = astar_search(g, h, 0, goal)
    path = make_node_path_from_last(last, goal)
    print(f"A* path from 0 to {goal}: {path}")
    print()


def greedy_search_example():
    """Greedy best-first search - fast but not always optimal."""
    print("=== Greedy Best-First Search ===")
    # Graph where greedy may not find the shortest path
    g = Graph(4, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 10.0)
    g.insert_edge(1, 3, 10.0)
    g.insert_edge(2, 3, 1.0)

    # Heuristic: distances to node 3
    h = [5.0, 8.0, 1.0, 0.0]

    last = greedy_search(g, h, 0, 3)
    path = make_node_path_from_last(last, 3)
    print(f"Greedy path from 0 to 3: {path}")
    print("(Greedy follows heuristic, not actual cost)")
    print()


def astar_vs_greedy():
    """Compare A* and greedy on the same graph."""
    print("=== A* vs Greedy Comparison ===")
    g = Graph(5, undirected=True)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 2, 3.0)
    g.insert_edge(1, 3, 5.0)
    g.insert_edge(2, 3, 1.0)
    g.insert_edge(3, 4, 1.0)

    h = [4.0, 3.0, 2.0, 1.0, 0.0]

    last_astar = astar_search(g, h, 0, 4)
    path_astar = make_node_path_from_last(last_astar, 4)

    last_greedy = greedy_search(g, h, 0, 4)
    path_greedy = make_node_path_from_last(last_greedy, 4)

    print(f"A* path:    {path_astar}")
    print(f"Greedy path: {path_greedy}")
    print()


def main():
    astar_example()
    greedy_search_example()
    astar_vs_greedy()


if __name__ == "__main__":
    main()
