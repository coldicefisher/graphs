
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


def depth_first_search_stack(g: Graph, start: int) -> list:
    seen: list = [False] * g.num_nodes
    last: list = [-1] * g.num_nodes
    
    to_explore: list = [start]
    to_explore.append(start)
    
    while to_explore:
        ind: int = to_explore.pop()
        if not seen[ind]:
            current: Node = g.nodes[ind]
            seen[ind] = True
            
            all_edges: list = current.get_edge_list()
            all_edges.reverse()
            for edge in all_edges:
                neighbor: int = edge.to_node
                if not seen[neighbor]:
                    last[neighbor] = ind
                    to_explore.append(neighbor)
                    
                    
                    
                    
def dfs_recursive_cc(g: Graph, ind: int, component: list, curr_comp: int):
    component[ind] = curr_comp
    
    current: Node = g.nodes[ind]
    
    for edge in current.get_edge_list():
        neighbor: int = edge.to_node
        if component[neighbor] == -1:
            dfs_recursive_cc(g, neighbor, component, curr_comp)
    
    
    
def dfs_connected_components(g: Graph) -> list:
    component: list = [-1] * g.num_nodes
    curr_comp: int = 0
    
    for ind in range(g.num_nodes):
        if component[ind] == -1:
            dfs_recursive_cc(g, ind, component, curr_comp)
            curr_comp = curr_comp + 1
            
    return component