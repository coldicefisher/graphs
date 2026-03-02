# graphs/shortest_paths/floyd_warshall.py


from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

import math

from typing import Union



def floyd_warshall(g: Graph) -> list[list[float]]:
    n = g.num_nodes
    dist = [[math.inf] * n for _ in range(n)]

    # distance to self is 0
    for i in range(n):
        dist[i][i] = 0.0

    # initialize from edges
    for node in g.nodes:
        for edge in node.get_edge_list():
            dist[edge.from_node][edge.to_node] = edge.weight

    # main triple loop
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist