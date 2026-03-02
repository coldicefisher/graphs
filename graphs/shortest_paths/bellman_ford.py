# graphs/shortest_paths/bellman_ford.py


from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

from typing import Union
import math


def bellman_ford(g: Graph, start_index: int) -> Union[list, None]:
    cost: list = [math.inf] * g.num_nodes
    last: list = [-1] * g.num_nodes
    all_edges: list = g.make_edge_list()
    cost[start_index] = 0.0
    
    for itr in range(g.num_nodes - 1):
        for edge in all_edges:
            cost_thr_node: float = cost[edge.from_node] + edge.weight
            if cost_thr_node < cost[edge.to_node]:
                cost[edge.to_node] = cost_thr_node
                last[edge.to_node] = edge.from_node
                
                
    for edge in all_edges:
        if cost[edge.to_node] > cost[edge.from_node] + edge.weight:
            return None
        
    return last
    
    

