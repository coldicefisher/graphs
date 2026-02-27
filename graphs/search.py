
from graphs.graph import Graph
from graphs.node import Node


def dfs_recursive_basic(g: Graph, ind: int, seen: list):
    seen[ind] = True
    
    current: Node = g.nodes[ind]
    
    for edge in current.get_edge_list():
        neighbor: int = edge.to_node
        if not seen[neighbor]:
            dfs_recursive_basic(g, neighbor, seen)
            
            
    
def depth_first_search_basic(g: Graph, start: int) -> list:
    seen: list = [False] * g.num_nodes
    dfs_recursive_basic(g, start, seen)
    
    
def depth_first_basic_all(g: Graph) -> list:
    seen: list = [False] * g.num_nodes
    
    for ind in range(g.num_nodes):
        if not seen[ind]:
            dfs_recursive_basic(g, ind, seen)
            
            
            
def dfs_recursive_path(g: Graph, ind: int, seen: list, last: list):
    seen[ind] = True
    
    current: Node = g.nodes[ind]
    
    for edge in current.get_edge_list():
        neighbor: int = edge.to_node
        if not seen[neighbor]:
            last[neighbor] = ind
            dfs_recursive_path(g, neighbor, seen, last)
            
            
def depth_first_search_path(g: Graph) -> list:
    seen: list = [False] * g.num_nodes
    last: list = [-1] * g.num_nodes
    
    for ind in range(g.num_nodes):
        if not seen[ind]:
            dfs_recursive_path(g, ind, seen, last)
            
    return last


