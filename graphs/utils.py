# graphs/utils.py

import math
from graphs.core.graph import Graph
from graphs.core.edge import Edge
from graphs.core.node import Node


def check_node_path_valid(g: Graph, path: list) -> bool:
    if len(path) == 0:
        return True

    for i in range(1, len(path)):
        if not g.is_edge(path[i - 1], path[i]):
            return False

    return True

    
def make_node_path_from_last(last: list, dest: int) -> list:
    result: list = []
    current: int = dest

    while current != -1:
        result.append(current)
        current = last[current]

    result.reverse()
    return result



def check_last_path_valid(g: Graph, last: list) -> bool:
    if len(last) != g.num_nodes:
        return False

    for to_node, from_node in enumerate(last):
        if from_node != -1 and not g.is_edge(from_node, to_node):
            return False

    return True

    
def compute_path_cost_from_edges(path: list) -> float:
    if len(path) == 0:
        return 0.0
    
    cost: float = 0.0
    prev_node: int = path[0].from_node
    for edge in path:
        if edge.from_node != prev_node:
            cost = math.inf
        
        else:
            cost = cost + edge.weight
        
        prev_node = edge.to_node
        
    return cost




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


def make_grid_with_obstacles(width: int, height: int, obstacles: set) -> Graph:
    num_nodes: int = width * height
    g: Graph = Graph(num_nodes, undirected=True)
    
    for r in range(height):
        for c in range(width):
            if (r, c) not in obstacles:
                index: int = r * width + c
                
                if (c < width -1) and (r, c + 1) not in obstacles:
                    g.insert_edge(index, index + 1, 1.0)
                if (r < height - 1) and (r + 1, c) not in obstacles:
                    g.insert_edge(index, index + width, 1.0)
                
    return g





def euclidean_dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
