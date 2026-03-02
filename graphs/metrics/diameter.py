# graphs/metrics/diameter.py

from typing import Union
import queue
import math

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

from graphs.traversal.bfs_search import breadth_first_search
from queue import PriorityQueue

from graphs.shortest_paths.floyd_warshall import FloydWarshall
   
   
   
   
# MAYBE NEW FILE ///////////////////////////////////////////////////////////////////////////////

def GraphDiameter(g: Graph) -> float:
    cost_matrix = FloydWarshall(g)
    max_cost = 0.0

    for i in range(g.num_nodes):
        for j in range(g.num_nodes):
            if cost_matrix[i][j] != -1:
                max_cost = max(max_cost, cost_matrix[i][j])

    return max_cost

# FROM THE BOOK

# def GraphDiameter(g: Graph) -> float:
#     last: list = FloydWarshall(g)
#     max_cost: float = -math.inf
    
#     for i in range(g.num_nodes):
#         for j in range(g.num_nodes):
#             cost: float = 0.0
#             current: int = j
            
#             while current != i:
#                 prev: int = last[i][current]
#                 if prev == -1:
#                     cost = math.inf
                    
#                     edge: Union[Edge, None] = g.get_edge(prev, current)
#                     cost = cost + edge.weight
#                     current = prev
                    
#             if cost > max_cost:
#                 max_cost = cost
                
#     return max_cost


