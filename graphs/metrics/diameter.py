# graphs/metrics/diameter.py

import math

from graphs.core.graph import Graph
from graphs.shortest_paths.floyd_warshall import floyd_warshall


def graph_diameter(g: Graph) -> float:
    cost_matrix = floyd_warshall(g)
    max_cost = 0.0

    for i in range(g.num_nodes):
        for j in range(g.num_nodes):
            if cost_matrix[i][j] != math.inf:
                max_cost = max(max_cost, cost_matrix[i][j])

    return max_cost
