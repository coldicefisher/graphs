# graphs/bfs_search.py
import queue

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.utils import make_node_path_from_last
from graphs.core.edge import Edge


def breadth_first_search(g: Graph, start: int) -> list:
    seen: list = [False] * g.num_nodes
    last: list = [-1] * g.num_nodes
    
    pending: queue.Queue = queue.Queue()
    pending.put(start)
    seen[start] = True
    
    while not pending.empty():
        index: int = pending.get()
        current: Node = g.nodes[index]
        
        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if not seen[neighbor]:
                pending.put(neighbor)
                seen[neighbor] = True
                last[neighbor] = index
                
    return last


def make_grid_graph(width: int, height: int) -> Graph:
    num_nodes: int = width * height
    g: Graph = Graph(num_nodes, undirected=True)
    
    for r in range(height):
        for c in range(width):
            index: int = r * width + c
            
            if (c < width - 1):
                g.insert_edge(index, index + 1, 1.0)
            if (r < height - 1):
                g.insert_edge(index, index + width, 1.0)
                
    return g



