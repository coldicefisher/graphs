"""
Chapter 16: Graph-Based Puzzles
Demonstrates solving the Prisoners and Guards river crossing puzzle.
"""

from graphs.puzzles.prisoners_guards import (
    PGState,
    pg_neighbors,
    create_prisoners_and_guards,
    pg_state_to_index_map,
    solve_pg_bfs,
    pq_generate_heuristic,
)
from graphs.shortest_paths.astar import astar_search
from graphs.utils import make_node_path_from_last


def puzzle_state_space():
    """Explore the state space of the Prisoners and Guards puzzle."""
    print("=== Prisoners & Guards State Space ===")
    g = create_prisoners_and_guards()
    print(f"Total states: {g.num_nodes}")
    print(f"Sample states:")
    for i in range(min(5, g.num_nodes)):
        print(f"  Node {i}: {g.nodes[i].label}")
    print()


def solve_with_bfs():
    """Solve the puzzle using BFS (shortest path)."""
    print("=== Solve with BFS ===")
    solve_pg_bfs()
    print()


def solve_with_astar():
    """Solve the puzzle using A* with a heuristic."""
    print("=== Solve with A* ===")
    g = create_prisoners_and_guards()
    h = pq_generate_heuristic(g)

    mapping = pg_state_to_index_map(g)
    start = mapping["3, 3, L"]
    goal = mapping["0, 0, R"]

    last = astar_search(g, h, start, goal)
    path = make_node_path_from_last(last, goal)

    print(f"A* solution ({len(path) - 1} moves):")
    for i, node_idx in enumerate(path):
        print(f"  Step {i}: {g.nodes[node_idx].label}")
    print()


def explore_neighbors():
    """Show the possible moves from the initial state."""
    print("=== Possible Moves from Start ===")
    initial = PGState(3, 3, "L")
    neighbors = pg_neighbors(initial)
    print(f"From {initial}:")
    for n in neighbors:
        print(f"  -> {n}")
    print()


def main():
    puzzle_state_space()
    explore_neighbors()
    solve_with_bfs()
    solve_with_astar()


if __name__ == "__main__":
    main()
