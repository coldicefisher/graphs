# graphs/shortest_paths/informed_search.py

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

from graphs.traversal.bfs_search import breadth_first_search
from graphs.traversal.dfs_search import depth_first_search_path

from typing import Union

from queue import PriorityQueue




def greedy_search(g: Graph, h: list, start: int, goal: int) -> list:
    visited: list = [False] * g.num_nodes
    last: list = [-1] * g.num_nodes
    pq: PriorityQueue = PriorityQueue(min_heap=True)
    pq.enqueue(start, h[start])
    while not pq.is_empty() and not visited[goal]:
        ind: int = pq.dequeue()
        current: Node = g.nodes[ind]
        visited[ind] = True
        
        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if not visited[neighbor] and not pq.in_queue(neighbor):
                pq.enqueue(neighbor, h[neighbor])
                last[neighbor] = ind
                
                
    return last
