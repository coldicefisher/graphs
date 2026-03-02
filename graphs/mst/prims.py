# graphs/mst/prims.py

from queue import PriorityQueue

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

from typing import Union

import math



    
def prims(g: Graph) -> Union[list, None]:
    pq: PriorityQueue = PriorityQueue()
    last: list = [-1] * g.num_nodes
    mst_edges: list = []
    
    pq.enqueue(0, 0.0)
    for i in range(1, g.num_nodes):
        pq.enqueue(i, float('inf'))
        
    while not pq.is_empty():
        index: int = pq.dequeue()
        current: Node = g.nodes[index]
        
        if last[index] != -1:
            mst_edges.append(current.get_edge(last[index]))
        elif index != 0:
            return None
        
        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if pq.in_queue(neighbor):
                
                if edge.weight < pq.get_priority(neighbor):
                    pq.update_priority(neighbor, edge.weight)
                    last[neighbor] = index
                    
                    
    return mst_edges

